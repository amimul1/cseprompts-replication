"""Load the original CSEPrompts 2.0 release (data/raw/CSEPrompts-main).

The released ``*.json`` files are JSON Lines (one object per line), and the
test cases are free text ("Test Case 1:\\nInput: ...\\nOutput: ...").  This
module reads them without modifying anything and parses the free-text tests
into (input, expected_output) pairs where the layout allows it.  Nothing here
makes the tests executable yet; that is the job of the harness (next step).
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_ROOT / "data" / "raw" / "CSEPrompts-main"

CODING_SPLITS = {
    "codingsites": RAW_DIR / "CodingSites" / "CodingSites.json",
    "academic": RAW_DIR / "Academic" / "Academic.json",
}
MCQ_PATH = RAW_DIR / "MCQ" / "MCQ_Prompts.json"

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


def load_coding(split: str) -> list[CodingPrompt]:
    rows = _read_jsonl(CODING_SPLITS[split])
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


def load_mcq() -> list[MCQ]:
    rows = _read_jsonl(MCQ_PATH)
    return [MCQ(f"mcq/{i:03d}", i, r["Prompt"], r["Answer"]) for i, r in enumerate(rows)]
