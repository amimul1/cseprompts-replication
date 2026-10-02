"""Helpers shared by the generated CSEPrompts pytest files.

Copied next to every generated test suite, so the suite is self-contained:
`pytest` + this file + conftest.py + cse_boot.py is all it needs.

Comparison rules (the `how` argument of check / check_stdout) are the only place
where output-format interpretation happens; each task's choice is recorded in
data/curation and in the generated test file header.
"""

from __future__ import annotations

import ast
import inspect
import json
import math
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BOOT = os.path.join(HERE, "cse_boot.py")
REL_TOL = 1e-6
ABS_TOL = 1e-9


class EntryPointMissing(Exception):
    """The function the task asks for does not exist in the candidate."""


# --------------------------------------------------------------------------- values

def deep_equal(actual, expected, seq_loose=False) -> bool:
    """== with float tolerance, applied recursively. Lists vs tuples differ unless seq_loose."""
    if isinstance(expected, bool) or isinstance(actual, bool):
        return actual == expected
    if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
        if isinstance(expected, int) and isinstance(actual, int):
            return actual == expected
        return math.isclose(actual, expected, rel_tol=REL_TOL, abs_tol=ABS_TOL)
    if isinstance(expected, (list, tuple)) and isinstance(actual, (list, tuple)):
        if not seq_loose and type(actual) is not type(expected):
            return False
        return len(actual) == len(expected) and all(deep_equal(a, e, seq_loose) for a, e in zip(actual, expected))
    if isinstance(expected, dict) and isinstance(actual, dict):
        return actual.keys() == expected.keys() and all(deep_equal(actual[k], expected[k], seq_loose) for k in expected)
    return actual == expected


def _materialize(actual):
    """Turn generators/iterators/map/filter objects into lists (e.g. 'write a generator function')."""
    if isinstance(actual, (str, bytes, list, tuple, dict, set, frozenset)) or actual is None:
        return actual
    if type(actual).__module__ == "numpy" and hasattr(actual, "tolist"):  # numpy arrays and scalars
        return actual.tolist()
    if hasattr(actual, "__next__") or inspect.isgenerator(actual) or type(actual).__name__ in ("map", "filter", "zip"):
        return list(actual)
    return actual


def check(actual, expected, how: str = "eq"):
    """Assert that a function's return value is acceptable.

    how:
      eq         == (float tolerance; list vs tuple strict)
      seq        like eq, but lists and tuples are interchangeable
      unordered  same elements, any order (multiset)
      any_of     expected is a list of acceptable values (eq to any one)
      str        str(actual) == expected
      true/false truthiness (for 'return True if ...' tasks where 1/0 is also fine)
    """
    actual = _materialize(actual)
    if how == "eq":
        ok = deep_equal(actual, expected)
    elif how == "seq":
        ok = deep_equal(actual, expected, seq_loose=True)
    elif how == "unordered":
        try:
            ok = sorted(map(repr, actual)) == sorted(map(repr, expected)) or deep_equal(
                sorted(actual), sorted(expected), seq_loose=True)
        except TypeError:
            ok = False
    elif how == "any_of":
        ok = any(deep_equal(actual, e) for e in expected)
    elif how == "str":
        ok = actual == expected or str(actual) == expected
    elif how in ("true", "false"):
        ok = bool(actual) is (how == "true")
    else:
        raise ValueError(f"unknown comparison {how!r}")
    assert ok, f"expected {expected!r}, got {actual!r} (comparison: {how})"


# --------------------------------------------------------------------------- functions

def _module_functions(m):
    out = []
    for name, obj in vars(m).items():
        if name.startswith("_"):
            continue
        if inspect.isfunction(obj) and getattr(obj, "__module__", None) == m.__name__:
            out.append((name, obj))
    return out


def _accepts(fn, nargs: int, kwargs) -> bool:
    try:
        inspect.signature(fn).bind(*([None] * nargs), **{k: None for k in kwargs})
        return True
    except (TypeError, ValueError):
        return False


def resolve_entry(m, entry: str | None, nargs: int, kwargs=()):
    """Find the function to test.

    If the prompt names the function (entry), use exactly that name. Otherwise
    (the prompt names none), pick among the candidate's top-level functions:
    the only one; else the only one accepting the test's arguments; else the
    only one not called by another; else the last defined such function.
    The choice is recorded in the test report.
    """
    if entry:
        obj = getattr(m, entry, None)
        if callable(obj):
            return entry, obj
        raise EntryPointMissing(f"candidate defines no function named {entry!r}")
    fns = _module_functions(m)
    if not fns:
        raise EntryPointMissing("candidate defines no top-level function")
    if len(fns) == 1:
        return fns[0]
    fitting = [(n, f) for n, f in fns if _accepts(f, nargs, kwargs)] or fns
    if len(fitting) == 1:
        return fitting[0]
    called = set()
    for _, f in fitting:
        called.update(getattr(f, "__code__", None).co_names if hasattr(f, "__code__") else ())
    roots = [(n, f) for n, f in fitting if n not in called] or fitting
    return max(roots, key=lambda nf: getattr(getattr(nf[1], "__code__", None), "co_firstlineno", 0))


RESOLVED: dict = {}


def call(m, task: dict, args=(), kwargs=None, entry: str | None = None):
    kwargs = kwargs or {}
    name, fn = resolve_entry(m, entry if entry is not None else task.get("entry"), len(args), kwargs)
    RESOLVED[name] = RESOLVED.get(name, 0) + 1
    return fn(*args, **kwargs)


def call_or_arg(m, task: dict, args=(), kwargs=None, entry: str | None = None):
    """For 'modify this dictionary/list' tasks: the return value, or the (mutated) first argument if None."""
    result = call(m, task, args, kwargs, entry)
    return args[0] if result is None and args else result


# --------------------------------------------------------------------------- programs

def substitute_vars(source: str, assignments: dict[str, str]) -> str:
    """Give top-level variables new values (GT CS1301 'we'll change these lines' tasks).

    Each existing top-level `name = ...` for a test variable gets the test value;
    variables the candidate never assigns are prepended. Values are Python source.
    """
    tree = ast.parse(source)
    done = set()
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name in assignments and name not in done:
                node.value = ast.parse(assignments[name], mode="eval").body
                done.add(name)
    missing = [n for n in assignments if n not in done]
    body = [ast.parse(f"{n} = {assignments[n]}").body[0] for n in missing]
    first_import_end = 0
    for i, node in enumerate(tree.body):  # keep `import datetime` etc. before prepended values that need them
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            first_import_end = i + 1
        else:
            break
    tree.body[first_import_end:first_import_end] = body
    return ast.unparse(ast.fix_missing_locations(tree))


class Run:
    def __init__(self, returncode, stdout, stderr, timed_out):
        self.returncode, self.stdout, self.stderr, self.timed_out = returncode, stdout, stderr, timed_out

    @property
    def error(self) -> str | None:
        if self.timed_out:
            return "Timeout"
        if self.returncode != 0:
            m = re.findall(r"^(\w+(?:Error|Exception|Exit|Interrupt)|StopIteration)\b", self.stderr, re.M)
            return m[-1] if m else f"exit {self.returncode}"
        return None


def run_program(path: str, stdin: str = "", assignments: dict | None = None, env: dict | None = None,
                timeout: float = 10.0) -> Run:
    """Run the candidate as a program (via cse_boot) with the given stdin."""
    target = path
    if assignments:
        with open(path, encoding="utf-8") as f:
            src = f.read()
        fd, target = tempfile.mkstemp(suffix=".py", dir=os.path.dirname(path))
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(substitute_vars(src, assignments))
    child_env = {"PATH": os.environ.get("PATH", ""), "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1",
                 "PYTHONIOENCODING": "utf-8", "LANG": "C.UTF-8", "HOME": os.path.dirname(path)}
    child_env.update({k: v for k, v in os.environ.items() if k.startswith("CSE_") and k != "CSE_CANDIDATE"})
    child_env.update(env or {})
    try:
        p = subprocess.run([sys.executable, "-I", BOOT, target], input=stdin, capture_output=True, text=True,
                           timeout=timeout, env=child_env, cwd=os.path.dirname(path))
        return Run(p.returncode, p.stdout, p.stderr, False)
    except subprocess.TimeoutExpired as e:
        out = e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
        return Run(-9, out, "", True)
    finally:
        if target != path:
            try:
                os.unlink(target)
            except OSError:
                pass


def _lines(text: str) -> list[str]:
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").split("\n")]
    while lines and not lines[-1]:
        lines.pop()
    while lines and not lines[0]:
        lines.pop(0)
    return lines


_NUM = re.compile(r"-?\d+(?:,\d{3})*(?:\.\d+)?")


def _numbers(text: str) -> list[float]:
    return [float(x.replace(",", "")) for x in _NUM.findall(text)]


def check_stdout(run: Run, expected, how: str = "tail"):
    """Assert that a program's stdout is acceptable. input() prompts never reach stdout.

    how:
      tail      the last len(expected lines) lines equal the expected lines (default)
      exact     all lines equal
      tail_ci   like tail, case-insensitive
      empty     prints nothing
      num       the last number printed equals expected (a number)
      nums      the numbers printed, in order, end with the expected list of numbers
      nums_in   the expected numbers appear consecutively somewhere in the printed numbers
      nums_in2  like nums_in, numbers compared to 2 decimal places
      suffix    like tail, but each line may carry a prefix (e.g. "Output: ")
      contains  expected (str) appears in stdout
      contains_ci  like contains, case-insensitive
      any_of    expected is a list of acceptable 'tail' outputs
    """
    assert not run.timed_out, "program timed out"
    assert run.returncode == 0, f"program crashed ({run.error}): {run.stderr[-500:]}"
    out = _lines(run.stdout)
    if how in ("tail", "exact", "tail_ci"):
        exp = _lines(expected)
        got = out[-len(exp):] if (how != "exact" and exp) else out
        if how == "tail_ci":
            ok = [g.lower() for g in got] == [e.lower() for e in exp]
        else:
            ok = got == exp
    elif how == "empty":
        ok = not out
    elif how == "num":
        nums = _numbers(run.stdout)
        ok = bool(nums) and math.isclose(nums[-1], float(expected), rel_tol=REL_TOL, abs_tol=1e-6)
    elif how == "nums":
        nums = _numbers(run.stdout)
        exp = [float(x) for x in (_numbers(expected) if isinstance(expected, str) else expected)]
        ok = len(nums) >= len(exp) and all(math.isclose(a, b, rel_tol=REL_TOL, abs_tol=1e-6)
                                           for a, b in zip(nums[-len(exp):], exp))
    elif how in ("nums_in", "nums_in2"):
        nums = _numbers(run.stdout)
        exp = [float(x) for x in (_numbers(expected) if isinstance(expected, str) else expected)]
        tol = 0.005 if how == "nums_in2" else 1e-6
        k = len(exp)
        ok = k > 0 and any(all(math.isclose(a, b, rel_tol=REL_TOL, abs_tol=tol) for a, b in zip(nums[i:i + k], exp))
                           for i in range(0, len(nums) - k + 1))
    elif how == "suffix":
        exp = _lines(expected)
        got = out[-len(exp):] if exp else out
        ok = len(got) == len(exp) and all(g.endswith(e) for g, e in zip(got, exp))
    elif how == "contains":
        ok = expected in run.stdout
    elif how == "contains_ci":
        ok = expected.lower() in run.stdout.lower()
    elif how == "any_of":
        ok = any(out[-len(_lines(e)):] == _lines(e) for e in expected)
    else:
        raise ValueError(f"unknown comparison {how!r}")
    assert ok, f"expected {expected!r}, got stdout {run.stdout[-800:]!r} (comparison: {how})"


def dump_json(path: str, obj) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, default=str)
