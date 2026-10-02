"""Turn the released free-text tests + curation into executable test specs and pytest files.

Two modes are produced from the same curation:
  original   the released test values, only mechanically cleaned (annotations such
             as "10 (1 + 2 + 3 + 4)" stripped, JSON true/false/null read as Python)
  validated  original + documented corrections: `fix` (wrong expected value, checked
             against the prompt and a reference solution), `drop` (ambiguous /
             out-of-spec / untestable test), `add` (authored tests, only for tasks
             whose release has no usable tests)
Tests that are not tests at all in the release (e.g. a header line such as
"Dot Product Test Cases:") are listed in `skip` and excluded from both modes.
"""

from __future__ import annotations

import ast
import copy
import importlib.util
import json
import re
import shutil
import textwrap
from dataclasses import dataclass, field
from pathlib import Path

from cseprompts.data import REPO_ROOT, CodingPrompt, load_coding

RUNTIME_DIR = Path(__file__).parent / "runtime"
CURATION_DIR = REPO_ROOT / "data" / "curation"
REFERENCE_DIR = REPO_ROOT / "data" / "reference"
SUITE_DIR = REPO_ROOT / "data" / "processed" / "pytest"
MODES = ("original", "validated")


class _Ref:
    def __repr__(self):
        return "REF"


REF = _Ref()          # "expected = whatever the reference solution returns/prints" (validated fixes only)
_NOTHING = object()


# --------------------------------------------------------------------------- literal parsing

_JSONISH = {"true": True, "false": False, "null": None, "True": True, "False": False, "None": None}


def _eval_node(node):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name) and node.id in _JSONISH:
        return _JSONISH[node.id]
    if isinstance(node, ast.List):
        return [_eval_node(e) for e in node.elts]
    if isinstance(node, ast.Tuple):
        return tuple(_eval_node(e) for e in node.elts)
    if isinstance(node, ast.Set):
        return {_eval_node(e) for e in node.elts}
    if isinstance(node, ast.Dict):
        return {_eval_node(k): _eval_node(v) for k, v in zip(node.keys, node.values)}
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        v = _eval_node(node.operand)
        return -v if isinstance(node.op, ast.USub) else +v
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "set" and not node.args:
        return set()
    raise ValueError(f"not a literal: {ast.dump(node)[:80]}")


def safe_literal(src: str):
    try:
        return _eval_node(ast.parse(src.strip(), mode="eval").body)
    except (SyntaxError, ValueError, TypeError, RecursionError):
        return _NOTHING


def strip_quotes(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'" and s.count(s[0]) == 2:
        return s[1:-1]
    return s


def _cut_points(t: str) -> list[int]:
    pts = sorted({m.start() for m in re.finditer(r" \(|\n| - |\s+#", t)})
    return pts


def parse_value(text: str):
    """Expected value of a function test: a Python/JSON literal, annotations stripped; else a string."""
    t = text.strip()
    v = safe_literal(t)
    if v is not _NOTHING:
        return v
    for p in _cut_points(t):
        v = safe_literal(t[:p])
        if v is not _NOTHING:
            return v
    return strip_quotes(t.split("\n\n")[0])


def parse_call_args(text: str, kw: tuple = (), unpack: bool = False, aslist: bool = False):
    """(args, kwargs) from inputs like '5, 2', 'a = 5, b = 5', '"hello"', 'f(10.0)', 'n = 5\\nr = 2'."""
    t = re.sub(r"\s+#[^\n]*$", "", text.strip())
    if aslist:
        v = safe_literal("[" + t + "]")
        if v is _NOTHING:
            raise ValueError(f"cannot read list from {text!r}")
        return (v,), {}
    call, called = None, None
    try:
        node = ast.parse(t, mode="eval").body
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id not in ("set",):
            call, called = node, node.func.id
    except SyntaxError:
        pass
    if call is None:
        try:
            call = ast.parse(f"__f({t})", mode="eval").body
        except SyntaxError:
            call = None
    if call is not None:
        args = [_eval_node(a) for a in call.args]
        kwargs = {}
        for k in call.keywords:
            val = _eval_node(k.value)
            if k.arg in kw:
                kwargs[k.arg] = val
            else:
                args.append(val)
    else:  # one assignment per line
        tree = ast.parse(t)
        args, kwargs = [], {}
        for st in tree.body:
            if not (isinstance(st, ast.Assign) and isinstance(st.targets[0], ast.Name)):
                raise ValueError(f"cannot read arguments from {text!r}")
            name, val = st.targets[0].id, _eval_node(st.value)
            if name in kw:
                kwargs[name] = val
            else:
                args.append(val)
    if unpack and len(args) == 1 and isinstance(args[0], tuple) and not kwargs:
        args = list(args[0])
    PARSE_INFO["called"] = called
    return tuple(args), kwargs


PARSE_INFO: dict = {}


def parse_assignments(text: str) -> dict[str, str]:
    """'goal = 50000\\nrate = 0.05' -> {'goal': '50000', 'rate': '0.05'} (values kept as Python source)."""
    tree = ast.parse(text.strip())
    out = {}
    for st in tree.body:
        if isinstance(st, ast.Assign) and isinstance(st.targets[0], ast.Name):
            out[st.targets[0].id] = ast.get_source_segment(text.strip(), st.value)
        else:
            raise ValueError(f"not an assignment: {ast.dump(st)[:80]}")
    return out


def _split_top(t: str, sep: str = ",") -> list[str]:
    """Split on sep outside quotes/brackets."""
    parts, depth, quote, cur = [], 0, None, ""
    for ch in t:
        if quote:
            cur += ch
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
        elif ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if ch == sep and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    return [p.strip() for p in parts if p.strip()]


def make_stdin(text: str, how: str = "text") -> str:
    t = text.strip()
    if how == "none":
        return ""
    if how == "text":
        return strip_quotes(t) + "\n"
    if how == "split":
        items = []
        for p in _split_top(t):
            if p.lower().replace("-", "").replace(" ", "") in ("controld", "ctrld"):
                break
            items.append(strip_quotes(p))
        return "\n".join(items) + "\n"
    if how == "values":
        return "\n".join(strip_quotes(v) for v in (p.split("=", 1)[1] for p in _split_top(t))) + "\n"
    raise ValueError(how)


def make_expected_output(text: str, how: str = "text") -> str:
    t = text.strip()
    if how == "text":
        return "\n".join(strip_quotes(ln) for ln in t.split("\n"))
    if how == "quoted_list":
        return "\n".join(strip_quotes(p) for p in _split_top(t))
    if how == "raw":
        return t
    if how == "last_number":
        nums = re.findall(r"-?\d+(?:\.\d+)?", t)
        return nums[-1] if nums else t
    raise ValueError(how)


# --------------------------------------------------------------------------- specs

@dataclass
class TestSpec:
    tid: str                         # "t3" = release test 3; "a1" = authored test
    kind: str
    args: tuple = ()
    kwargs: dict = field(default_factory=dict)
    expected: object = None
    stdin: str | None = None
    assignments: dict | None = None
    code: str | None = None
    how: str | None = None
    entry: str | None = None          # per-test entry override (multi-function tasks)
    env: dict | None = None
    release: str | None = None        # the released text, for the file comment
    change: str | None = None         # validated-mode change note


@dataclass
class TaskSpec:
    uid: str
    split: str
    number: int
    prompt: str
    kind: str
    entry: str | None
    how: str
    well_posed: bool
    issues: list
    note: str
    env: dict | None
    tests: dict                       # mode -> list[TestSpec]
    skipped: dict                     # release test id -> reason
    fixed: dict                       # tid -> {"from":..., "to":..., "why":...}
    dropped: dict                     # tid -> reason
    added: list
    use_arg_if_none: bool = False


def load_curation(split: str) -> dict:
    path = CURATION_DIR / f"{split}.py"
    spec = importlib.util.spec_from_file_location(f"curation_{split}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.TASKS


def _auto_tests(p: CodingPrompt, c: dict) -> list[TestSpec]:
    kind = c["kind"]
    out = []
    for i, t in enumerate(p.tests, 1):
        tid = f"t{i}"
        if i in c.get("skip", {}):
            continue
        release = t.raw
        if not t.parsed:
            raise ValueError(f"{p.uid} {tid}: release test not parseable; add it to skip or give explicit tests")
        over = c.get("per_test", {}).get(i, {})
        how = over.get("how", c.get("how"))
        if kind == "function":
            PARSE_INFO.clear()
            args, kwargs = parse_call_args(t.input, tuple(c.get("kw", ())), c.get("unpack", False),
                                           c.get("aslist", False))
            expected = over["expected"] if "expected" in over else parse_value(t.expected_output)
            entry = over.get("entry")
            if entry is None and c.get("entry_from_call") and PARSE_INFO.get("called"):
                entry = PARSE_INFO["called"]
            out.append(TestSpec(tid, kind, args, kwargs, expected, how=how, release=release, entry=entry))
        elif kind == "program":
            stdin = over.get("stdin", make_stdin(t.input, c.get("stdin", "text")))
            expected = over["expected"] if "expected" in over else make_expected_output(
                t.expected_output, c.get("out", "text"))
            out.append(TestSpec(tid, kind, stdin=stdin, expected=expected, how=how, release=release,
                                env=over.get("env")))
        elif kind == "vars":
            assignments = parse_assignments(t.input)
            expected = over["expected"] if "expected" in over else make_expected_output(
                t.expected_output, c.get("out", "text"))
            out.append(TestSpec(tid, kind, assignments=assignments, expected=expected, how=how, release=release))
        else:
            raise ValueError(f"{p.uid}: kind {kind!r} needs explicit tests")
    return out


def _explicit_tests(p: CodingPrompt, c: dict, key: str, prefix: str) -> list[TestSpec]:
    out = []
    release = {f"t{i}": t.raw for i, t in enumerate(p.tests, 1)}
    for j, t in enumerate(c[key], 1):
        tid = t.get("id", f"{prefix}{j}")
        out.append(TestSpec(tid, c["kind"], tuple(t.get("args", ())), t.get("kwargs", {}), t.get("expected"),
                            stdin=t.get("stdin"), assignments=t.get("assignments"), code=t.get("code"),
                            how=t.get("how", c.get("how")), entry=t.get("entry"), env=t.get("env"),
                            release=release.get(tid)))
    return out


def build_task(p: CodingPrompt, c: dict, reference_value) -> TaskSpec:
    kind = c["kind"]
    default_how = c.get("how") or ("eq" if kind in ("function", "custom") else "tail")
    c = {**c, "how": default_how}
    original = _explicit_tests(p, c, "tests", "t") if "tests" in c else _auto_tests(p, c)
    validated, fixed, dropped = [], {}, {}
    if not c.get("well_posed", True):
        return TaskSpec(p.uid, p.split, p.number, p.prompt, kind, c.get("entry"), default_how, False,
                        c.get("issues", []), c.get("note", ""), c.get("env"),
                        {"original": original, "validated": []},
                        {f"t{i}": r for i, r in c.get("skip", {}).items()}, {},
                        {t.tid: "task not well-posed: " + "; ".join(c.get("issues", [])) for t in original}, [],
                        c.get("use_arg_if_none", False))
    for t in original:
        n = int(t.tid[1:]) if re.fullmatch(r"t\d+", t.tid) else None
        if n in c.get("drop", {}):
            dropped[t.tid] = c["drop"][n]
            continue
        if n in c.get("fix", {}):
            f = c["fix"][n]
            new = copy.deepcopy(t)  # a shallow copy shares args with the original-mode test
            for k in ("expected", "how", "stdin", "args", "kwargs", "assignments", "code", "env", "entry"):
                if k in f:
                    setattr(new, k, f[k])
            if new.expected is REF:
                new.expected = reference_value(p, c, new)
            new.change = f["why"]
            fixed[t.tid] = {"from": repr(t.expected), "to": repr(new.expected), "why": f["why"]}
            validated.append(new)
        else:
            validated.append(t)
    added = []
    if "add" in c:
        for t in _explicit_tests(p, c, "add", "a"):
            if t.expected is REF:
                t.expected = reference_value(p, c, t)
            t.change = "authored (release has no usable tests for this task)"
            validated.append(t)
            added.append(t.tid)
    for mode_tests in (original, validated):
        for t in mode_tests:
            if (t.how or default_how) == "num":
                try:
                    float(t.expected)
                except (TypeError, ValueError):
                    raise ValueError(f"{p.uid} {t.tid}: comparison 'num' needs a number, got {t.expected!r} "
                                     "(use out='last_number')") from None
    return TaskSpec(p.uid, p.split, p.number, p.prompt, kind, c.get("entry"), default_how,
                    c.get("well_posed", True), c.get("issues", []), c.get("note", ""), c.get("env"),
                    {"original": original, "validated": validated},
                    {f"t{i}": r for i, r in c.get("skip", {}).items()}, fixed, dropped, added,
                    c.get("use_arg_if_none", False))


# --------------------------------------------------------------------------- reference execution (build time)

def reference_path(uid: str) -> Path:
    split, num = uid.split("/")
    return REFERENCE_DIR / split / f"{num}.py"


def make_reference_value():
    """Callable computing a test's expected value by running the reference solution."""
    import sys

    sys.path.insert(0, str(RUNTIME_DIR))
    import cse_runtime  # noqa: E402

    cache = {}

    def value(p: CodingPrompt, c: dict, t: TestSpec):
        path = reference_path(p.uid)
        if t.kind == "function":
            if path not in cache:
                spec = importlib.util.spec_from_file_location(f"ref_{p.split}_{p.number}", path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                cache[path] = mod
            mod = cache[path]
            fn = getattr(mod, t.entry or c.get("entry") or mod.ENTRY)
            # copies: a reference that mutates its input must not change the test's recorded input
            return cse_runtime._materialize(fn(*copy.deepcopy(t.args), **copy.deepcopy(t.kwargs)))
        run = cse_runtime.run_program(str(path), stdin=t.stdin or "", assignments=t.assignments,
                                      env={**(c.get("env") or {}), **(t.env or {})})
        if run.returncode != 0:
            raise RuntimeError(f"reference for {p.uid} crashed: {run.stderr[-400:]}")
        text = "\n".join(cse_runtime._lines(run.stdout))
        if (t.how or c.get("how")) == "num":  # number-only comparison: keep the last number printed
            nums = re.findall(r"-?\d+(?:\.\d+)?", text.replace(",", ""))
            return nums[-1] if nums else text
        return text

    return value


# --------------------------------------------------------------------------- pytest file generation

def _comment(text: str | None, width: int = 110) -> str:
    if not text:
        return ""
    one = text.replace("\n", "\\n")
    return textwrap.shorten(one, width=width, placeholder=" ...")


def render_test_file(task: TaskSpec, mode: str) -> str:
    tests = task.tests[mode]
    head = [
        "# AUTO-GENERATED by scripts/build_tasks.py -- do not edit.",
        f"# Edit data/curation/{task.split}.py (and data/reference/{task.split}/) instead, then rebuild.",
        f"# Task {task.uid} | mode: {mode} | kind: {task.kind} | entry: {task.entry} | comparison: {task.how}",
        f"# Well-posed: {'yes' if task.well_posed else 'NO -- ' + '; '.join(task.issues)}",
    ]
    if task.note:
        head += [f"# Note: {line}" for line in textwrap.wrap(task.note, 100)]
    head += [f"# Prompt: {_comment(task.prompt, 150)}", "",
             "import pytest  # noqa: F401",
             "from cse_runtime import call, call_or_arg, check, check_stdout, run_program  # noqa: F401", "",
             f"TASK = {{'uid': {task.uid!r}, 'kind': {task.kind!r}, 'entry': {task.entry!r}}}",
             f"ENV = {task.env!r}", ""]
    body = []
    for t in tests:
        how = t.how or task.how
        lines = [f"def test_{t.tid}({'m' if task.kind in ('function', 'custom') else 'candidate_path'}):"]
        if t.release:
            lines.append(f"    # release: {_comment(t.release, 104)}")
        if t.change:
            lines.append(f"    # VALIDATED CHANGE: {_comment(t.change, 96)}")
        if task.kind == "function" and t.code:
            lines += ["    " + ln for ln in textwrap.dedent(t.code).strip().splitlines()]
        elif task.kind == "function":
            entry = f", entry={t.entry!r}" if t.entry else ""
            caller = "call_or_arg" if task.use_arg_if_none else "call"
            lines.append(f"    check({caller}(m, TASK, {t.args!r}, {t.kwargs!r}{entry}), {t.expected!r}, {how!r})")
        elif task.kind == "custom":
            lines += ["    " + ln for ln in textwrap.dedent(t.code).strip().splitlines()]
        else:
            env = {**(task.env or {}), **(t.env or {})}
            kw = [f"stdin={t.stdin!r}"] if t.stdin is not None else []
            if t.assignments:
                kw.append(f"assignments={t.assignments!r}")
            if env:
                kw.append(f"env={env!r}")
            lines.append(f"    check_stdout(run_program(candidate_path, {', '.join(kw)}), {t.expected!r}, {how!r})")
        body.append("\n".join(lines))
    if not tests:
        body.append("# This task has no usable tests in this mode (see the manifest).")
    return "\n".join(head) + "\n\n" + "\n\n\n".join(body) + "\n"


def write_suite(tasks: list[TaskSpec], out_root: Path = SUITE_DIR) -> None:
    for mode in MODES:
        root = out_root / mode
        if root.exists():
            shutil.rmtree(root)
        root.mkdir(parents=True)
        for f in ("conftest.py", "cse_runtime.py", "cse_boot.py"):
            shutil.copy(RUNTIME_DIR / f, root / f)
        (root / "pytest.ini").write_text("[pytest]\naddopts = -p no:cacheprovider\n")
        manifest = []
        for task in tasks:
            d = root / task.split
            d.mkdir(exist_ok=True)
            (d / f"test_{task.number:03d}.py").write_text(render_test_file(task, mode), encoding="utf-8")
            manifest.append({
                "uid": task.uid, "kind": task.kind, "entry": task.entry, "comparison": task.how,
                "well_posed": task.well_posed, "issues": task.issues,
                "test_file": f"{task.split}/test_{task.number:03d}.py",
                "tests": [t.tid for t in task.tests[mode]], "n_tests": len(task.tests[mode]),
                "skipped_release_fragments": task.skipped,
                **({"fixed": task.fixed, "dropped": task.dropped, "added": task.added} if mode == "validated" else {}),
                "note": task.note,
            })
        with (root / "tasks.jsonl").open("w", encoding="utf-8") as f:
            for row in manifest:
                f.write(json.dumps(row) + "\n")


def build_all(splits=("codingsites", "academic")) -> list[TaskSpec]:
    value = make_reference_value()
    tasks = []
    for split in splits:
        cur = load_curation(split)
        for p in load_coding(split):
            if p.number not in cur:
                raise KeyError(f"{p.uid} has no curation entry")
            tasks.append(build_task(p, cur[p.number], value))
    return tasks
