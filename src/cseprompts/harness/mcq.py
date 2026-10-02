"""Multiple-choice questions: answer keys (release vs validated) and grading.

The release has 100 MCQ records (60 distinct questions).
  release    all 100 items; accepted = the option(s) the release key matches (paper-comparable)
  validated  the distinct items with checked keys from data/curation/mcq.py (a later benchmark
             version; optional, not part of the paper replication)
Answers are option NUMBERS (0-based, in the order options() reads them): several options differ
only in indentation, so option text cannot identify an answer.
Grading follows the paper's MCQ rubric (Guidelines.csv): 0 incorrect, 1 partially correct (a correct
option is among several the response picks), 2 correct. Where the question accepts any of several
correct options, picking only correct ones is 2.
"""

from __future__ import annotations

import importlib.util
import re

from cseprompts.data import REPO_ROOT, load_mcq


CURATION = REPO_ROOT / "data" / "curation" / "mcq.py"


def has_validated_keys() -> bool:
    return CURATION.exists()  # a repo may ship only the release keys


def _curation():
    if not has_validated_keys():
        return {}, {}
    spec = importlib.util.spec_from_file_location("curation_mcq", CURATION)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.ACCEPT, mod.EXCLUDE


def norm(s: str) -> str:
    return " ".join(s.replace(" ", " ").split()).strip().rstrip(".").lower()


def _match(s: str) -> str:
    # release keys write "a = 1, b = 2" where options use two lines, and one key (mcq/022) keeps CSV-escaped
    # doubled quotes; neither changes which option a human grader would read the key as
    return norm(s.replace('""', '"').replace(",", " "))


def release_accept(opts: list[str], key: str) -> list[int]:
    """Option numbers the release key matches: the whole key, else each of its lines (multi-answer keys)."""
    names = [_match(o) for o in opts]
    whole = [i for i, n in enumerate(names) if n == _match(key)]
    if whole:
        return whole
    parts = [p for p in key.split("\n") if p.strip()]
    if len(parts) < 2:
        return []
    return sorted({i for p in parts for i, n in enumerate(names) if n == _match(p)})


def items(mode: str) -> list[dict]:
    if mode == "validated" and not has_validated_keys():
        raise ValueError(f"validated MCQ keys need {CURATION}")
    accept_fix, exclude = _curation()
    out, seen = [], set()
    for q in load_mcq():
        opts = options(q.prompt)
        accept = release_accept(opts, q.answer)
        if mode == "validated":
            if norm(q.prompt) in seen:
                continue
            seen.add(norm(q.prompt))
            if q.uid in exclude:
                continue
            if q.uid in accept_fix:
                accept, n, _why = accept_fix[q.uid]
                if n != len(opts):
                    raise ValueError(f"{q.uid}: data/curation/mcq.py expects {n} options, the parser finds {len(opts)}")
            if not accept:
                raise ValueError(f"{q.uid}: no accepted option; add it to data/curation/mcq.py")
        out.append({"uid": q.uid, "prompt": q.prompt, "options": opts, "accept": sorted(accept),
                    "release_key": q.answer})
    return out


def options(prompt: str) -> list[str]:
    """Best-effort option list: blocks after the last question line (used only for auto suggestions)."""
    lines = prompt.split("\n")
    qline = max((i for i, ln in enumerate(lines) if "?" in ln or ln.strip().lower().startswith("pick one")), default=-1)
    rest = "\n".join(lines[qline + 1:])
    blocks = [b.strip() for b in re.split(r"\n\s*\n", rest) if b.strip()]
    if len(blocks) <= 1:
        blocks = [ln.strip() for ln in rest.split("\n") if ln.strip()]
    return blocks


READER_VERSION = "2.0"  # rules: docs/MANUAL_CLEANING.md, "MCQ answers"

# Statements in which a response commits to an answer. The LAST one in the response counts.
_STATEMENTS = [
    re.compile(r"(?i)\b(?:correct|right|final)\s+(?:answer|option|value|choice|output)s?\b"),
    re.compile(r"(?i)\bthe output of (?:the|this) (?:line of )?(?:code|python code)\b"),
]
_RESOLVES = re.compile(r"(?i)\bresolves to (True|False)\b")
_QUOTED_CORRECT = re.compile(r'(?i)"([^"\n]+)" is (?:the )?correct')
_LIST_ITEM = re.compile(r"^\s*(?:[-*\u2022]|\d+[.)])\s+")
_OPTION_REF = re.compile(r"(?i)\boption\s+(\d+)\b")


def _rnorm(s: str) -> str:
    """Normalisation used to find option text inside a response (applied to options and response alike)."""
    lines = [_LIST_ITEM.sub("", ln) for ln in s.replace("\u00a0", " ").split("\n")]
    t = " ".join(lines).replace("`", "").replace(";", " ").replace(",", " ")
    t = re.sub(r"\band\b", " ", t.lower())
    return " ".join(t.split()).strip().rstrip(".:").strip()


def _statement_blocks(response: str, opts: list[str]) -> list[dict]:
    """Every answer statement, in order: {pos, marker, inline, items} (items = the answer's list items)."""
    option_names = {_rnorm(o) for o in opts}
    out = []
    for rx in _STATEMENTS:
        for m in rx.finditer(response):
            line_end = response.find("\n", m.end())
            line_end = len(response) if line_end < 0 else line_end
            rest = response[m.end():line_end]
            inline = ":" not in rest
            if inline:  # "The correct options are 5, 6, and 8." / "the correct answer is option 4."
                first = re.sub(r"(?i)^.*?\b(?:is|are|would be|will be)\b", "", rest, count=1)
            else:
                first = rest.split(":", 1)[1]
            block = [first.strip()] if first.strip() else []
            if not inline:
                for p in re.split(r"\n\s*\n", response[line_end:]):
                    if not p.strip():
                        continue
                    if not block or _LIST_ITEM.match(p) or _rnorm(p) in option_names:
                        block.append(p.strip())
                    else:
                        break
            out.append({"pos": m.start(), "marker": m.group(0), "inline": inline, "items": _split_items(block)})
    out += [{"pos": m.start(), "marker": "resolves to", "inline": False, "items": [m.group(1)]}
            for m in _RESOLVES.finditer(response)]
    out += [{"pos": m.start(), "marker": "is correct", "inline": False, "items": [m.group(1)]}
            for m in _QUOTED_CORRECT.finditer(response)]
    return sorted(out, key=lambda d: d["pos"])


def _split_items(paragraphs: list[str]) -> list[str]:
    """A list answer ("- a", "1. b") becomes one item per entry; continuation lines stay with their entry."""
    items = []
    for para in paragraphs:
        for ln in para.split("\n"):
            if _LIST_ITEM.match(ln) or not items:
                items.append(ln)
            else:
                items[-1] += "\n" + ln
    return items


def _options_in(text: str, opts: list[str]) -> list[int]:
    """Options whose (normalised) text appears in `text`; an occurrence inside a longer matched option
    does not count (so "2" inside "2.1" or "if x:" inside "elif x:" is ignored)."""
    t = _rnorm(text)
    hits = []
    for i, o in enumerate(opts):
        n = _rnorm(o)
        if not n:
            continue
        for m in re.finditer(re.escape(n), t):
            a, b = m.start(), m.end()
            before_ok = a == 0 or not (t[a - 1].isalnum() or t[a - 1] in "_.\"")
            after_ok = b == len(t) or not (t[b].isalnum() or t[b] in "_\"") and \
                not (t[b] == "." and b + 1 < len(t) and t[b + 1].isalnum())
            if before_ok and after_ok:
                hits.append((a, b, i))
    keep = {i for a, b, i in hits
            if not any(a2 <= a and b <= b2 and (b2 - a2) > (b - a) for a2, b2, _ in hits)}
    return sorted(keep)


def _numbers(statement: dict, opts: list[str]) -> list[int]:
    found = set()
    for item in statement["items"]:
        found |= set(_options_in(item, opts))
        found |= {int(n) - 1 for n in _OPTION_REF.findall(item) if 0 < int(n) <= len(opts)}
    text = " ".join(statement["items"])
    if "option" in statement["marker"].lower() and re.fullmatch(r"(?i)[\d\s,&.]*(?:and[\d\s,&.]*)*", text):
        found |= {int(n) - 1 for n in re.findall(r"\d+", text) if 0 < int(n) <= len(opts)}
    return sorted(found)


def read_choice(response: str, opts: list[str]) -> dict:
    """The option number(s) a response chooses, by the rules in docs/MANUAL_CLEANING.md ("MCQ answers"):
    the last explicit answer statement counts (a trailing inline remark that names no option, such as
    "the correct options are the ones that...", is skipped); its text is matched to the options, or
    "option N" to the N-th listed option; an answer that is not one of the options counts as no choice."""
    statements = _statement_blocks(response, opts)
    if not statements:
        return {"numbers": [], "note": "no answer statement", "statement": ""}
    for st in reversed(statements):
        numbers = _numbers(st, opts)
        if numbers or not st["inline"]:
            break
    note = f"{len(statements)} answer statement(s); used: '{st['marker']}'"
    if not numbers:
        note += "; stated answer is not one of the options"
    return {"numbers": numbers, "note": note, "statement": " / ".join(st["items"])[:200]}


def auto_choice(response: str, opts: list[str]) -> list[str]:
    """Option texts chosen by read_choice (kept for older callers)."""
    return [opts[i] for i in read_choice(response, opts)["numbers"]]


def choice_numbers(texts: list[str], opts: list[str]) -> list[int]:
    """Option numbers for option texts; the first match when options repeat."""
    names = [norm(o) for o in opts]
    return sorted({names.index(norm(t)) for t in texts if norm(t) in names})


def grade(picks: list[int], accept: list[int]) -> int:
    """0/1/2 per the paper's rubric, for option numbers."""
    picks, ok = set(picks), set(accept)
    if not picks & ok:
        return 0
    return 2 if picks <= ok else 1
