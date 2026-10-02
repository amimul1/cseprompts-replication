"""Reading generation runs and locating manual-cleaning files."""

from __future__ import annotations

import json
import re
from pathlib import Path

from cseprompts.data import REPO_ROOT

ANNOTATION_DIR = REPO_ROOT / "annotations" / "manual_cleaning"
STATUS_RE = re.compile(r"^# MANUAL_STATUS:\s*(TODO|DONE|NO_CODE)\s*$", re.M)
HEADER_END = "# ---- model response below: edit from here ----"


def load_run(run_dir: Path) -> dict:
    run_dir = Path(run_dir)
    meta = json.loads((run_dir / "run_meta.json").read_text())
    prompts = {}
    for line in (run_dir / "prompts.jsonl").read_text().splitlines():
        if line.strip():
            row = json.loads(line)
            prompts[row["uid"]] = row
    samples = []
    for split in meta["splits"]:
        path = run_dir / f"{split}.jsonl"
        if path.exists():
            samples += [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    return {"dir": run_dir, "meta": meta, "prompts": prompts, "samples": samples}


def run_id(meta: dict) -> tuple[str, str]:
    name = meta["protocol_name"] + (f"__limit{meta['limit']}" if meta.get("limit") else "")
    return meta["model_key"], name


def manual_file(model_key: str, run_name: str, uid: str, sample: int) -> Path:
    split, num = uid.split("/")
    return ANNOTATION_DIR / model_key / run_name / split / f"{num}__s{sample:02d}.py"


def manual_status(text: str) -> str:
    m = STATUS_RE.search(text)
    return m.group(1) if m else "TODO"


def manual_code(text: str) -> str:
    """The code part of a manual-cleaning file (everything after the header)."""
    return text.split(HEADER_END, 1)[1] if HEADER_END in text else text
