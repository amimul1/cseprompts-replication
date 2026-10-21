"""Load a CSEPrompts 2.0 release (data/raw/).

Two releases are kept, byte-identical to GitHub mraihan-gmu/CSEPrompts:
  - 57275c2 (2026-10-11, "fixed test case issues"): the CURRENT release and the default.
  - 58d7ea0 (2024-09-25): the original release used by the paper. OUTDATED; kept only to reproduce
    results that were computed on it. Select it with the environment variable CSE_RELEASE=58d7ea0.

The released ``*.json`` files are JSON Lines (one object per line), and the
test cases are free text ("Test Case 1:\\nInput: ...\\nOutput: ...").  This
module reads them without modifying anything and parses the free-text tests
into (input, expected_output) pairs where the layout allows it.  Nothing here
makes the tests executable yet; that is the job of the harness (next step).
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CURRENT_RELEASE = "57275c2"
OUTDATED_RELEASES = ("58d7ea0",)
# Folder names under data/raw/ (the first that exists is used).
RELEASE_DIRS = {
    "57275c2": ("CSEPrompts-57275c2",),
    "58d7ea0": ("CSEPrompts-main", "OUTDATED_CSEPrompts-58d7ea0"),
}
RELEASE = os.environ.get("CSE_RELEASE", CURRENT_RELEASE)
if RELEASE not in RELEASE_DIRS:
    raise ValueError(f"CSE_RELEASE={RELEASE!r}; choose one of {sorted(RELEASE_DIRS)}")


def release_dir(release: str | None = None) -> Path:
    names = RELEASE_DIRS[release or RELEASE]
    for name in names:
        d = REPO_ROOT / "data" / "raw" / name
        if d.exists():
            return d
    return REPO_ROOT / "data" / "raw" / names[0]


def release_paths(release: str | None = None) -> tuple[dict, Path]:
    d = release_dir(release)
    return ({"codingsites": d / "CodingSites" / "CodingSites.json", "academic": d / "Academic" / "Academic.json"},
            d / "MCQ" / "MCQ_Prompts.json")


RAW_DIR = release_dir()
CODING_SPLITS, MCQ_PATH = release_paths()

_CASE_SPLIT = re.compile(r"Test Case\s*\d+\s*:", re.IGNORECASE)
_INPUT_LABEL = r"(?:Input|Function Call|Call)"
_OUTPUT_LABEL = r"(?:Expected Output|Output)"
_CASE_BODY = re.compile(
    rf"\A\s*{_INPUT_LABEL}\s*:[ \t]*(?P<inp>.*?)\s*^[ \t]*{_OUTPUT_LABEL}\s*:\s*(?P<out>.*)\Z",
    re.IGNORECASE | re.DOTALL | re.MULTILINE,
)


@dataclass
class TestCase:
    raw: str
    input: str | None = None
    expected_output: str | None = None

    @property
    def parsed(self) -> bool:
        return self.input is not None and self.expected_output is not None


@dataclass
class CodingPrompt:
    uid: str  # e.g. "codingsites/001"
    split: str
    number: int
    prompt: str
    tests_raw: str
    tests: list[TestCase] = field(default_factory=list)


@dataclass
class MCQ:
    uid: str  # e.g. "mcq/000" (0-based line index; the release has no ids)
    index: int
    prompt: str
    answer: str


def _read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def parse_test_cases(text: str) -> list[TestCase]:
    chunks = [c.strip() for c in _CASE_SPLIT.split(text) if c.strip()]
    cases = []
    for chunk in chunks:
        m = _CASE_BODY.search(chunk)
        if m:
            cases.append(TestCase(chunk, m.group("inp").strip(), m.group("out").strip()))
        else:
            cases.append(TestCase(chunk))
    return cases


def load_coding(split: str, release: str | None = None) -> list[CodingPrompt]:
    rows = _read_jsonl(release_paths(release)[0][split])
    return [
        CodingPrompt(
            uid=f"{split}/{int(r['#']):03d}",
            split=split,
            number=int(r["#"]),
            prompt=r["Prompt"],
            tests_raw=r["Test Cases"],
            tests=parse_test_cases(r["Test Cases"]),
        )
        for r in rows
    ]


def load_mcq(release: str | None = None) -> list[MCQ]:
    rows = _read_jsonl(release_paths(release)[1])
    return [MCQ(f"mcq/{i:03d}", i, r["Prompt"], r["Answer"]) for i, r in enumerate(rows)]
