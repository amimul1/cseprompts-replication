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


_ANSWER = re.compile(r"(?i)(?:correct|final)?\s*(?:answer|option)\s*(?:is|would be|will be)?\s*[:\-]?\s*(.+)")


def auto_choice(response: str, opts: list[str]) -> list[str]:
    """Heuristic: the option(s) the response commits to (checked in order: 'answer is X' lines, bold text,
    first line). Returns [] if nothing matches. Only a suggestion for the human annotator."""
    explicit = [m.group(1) for m in _ANSWER.finditer(response)]
    bold = re.findall(r"\*\*(.+?)\*\*", response, re.S)
    first = next((ln for ln in response.splitlines() if ln.strip()), "")
    candidates = explicit + bold + [first]
    nopts = [(o, norm(o)) for o in opts]
    clean = [norm(c.strip("`*: ")) for c in candidates]
    for c in clean:  # 1) a candidate that IS one option
        exact = [o for o, n in nopts if n and (c == n or c == n.strip('"'))]
        if exact:
            return exact
    if explicit or bold:  # 2) the model's own stated answer, even if option parsing failed
        return [(explicit or bold)[0].strip("`*: .")]
    for c in clean:  # 3) options mentioned inside the first line
        contained = [o for o, n in nopts if n and len(n) > 1 and n in c]
        if contained:
            return contained
    return []


def choice_numbers(texts: list[str], opts: list[str]) -> list[int]:
    """Option numbers for option texts (e.g. auto_choice output); the first match when options repeat."""
    names = [norm(o) for o in opts]
    return sorted({names.index(norm(t)) for t in texts if norm(t) in names})


def grade(picks: list[int], accept: list[int]) -> int:
    """0/1/2 per the paper's rubric, for option numbers."""
    picks, ok = set(picks), set(accept)
    if not picks & ok:
        return 0
    return 2 if picks <= ok else 1
