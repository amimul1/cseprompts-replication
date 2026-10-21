"""Reading generation runs and locating manual-cleaning files."""

from __future__ import annotations

import json
import re
from pathlib import Path

from cseprompts.data import RELEASE, REPO_ROOT

ANNOTATION_DIR = REPO_ROOT / "annotations" / "manual_cleaning"
STATUS_RE = re.compile(r"^# MANUAL_STATUS:\s*(TODO|DONE|NO_CODE)\s*$", re.M)
HEADER_END = "# ---- model response below: edit from here ----"


def load_run(run_dir: Path) -> dict:
    run_dir = Path(run_dir)
    meta = json.loads((run_dir / "run_meta.json").read_text())
    if run_release(meta) != RELEASE:
        raise SystemExit(f"{run_dir} was generated from CSEPrompts release {run_release(meta)}, but the code is set to "
                         f"{RELEASE}; run this command with CSE_RELEASE={run_release(meta)}.")
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


def run_release(meta: dict) -> str:
    """The CSEPrompts release a run's prompts came from (runs made before this was recorded used 58d7ea0)."""
    return meta.get("dataset_release", "58d7ea0")


def run_name(protocol: str, limit=None, release: str = RELEASE) -> str:
    """Runs on the original release keep their old names; later releases get a suffix (e.g. greedy__57275c2)."""
    return protocol + (f"__limit{limit}" if limit else "") + ("" if release == "58d7ea0" else f"__{release}")


def run_id(meta: dict) -> tuple[str, str]:
    return meta["model_key"], run_name(meta["protocol_name"], meta.get("limit"), run_release(meta))


def manual_file(model_key: str, run_name: str, uid: str, sample: int) -> Path:
    split, num = uid.split("/")
    return ANNOTATION_DIR / model_key / run_name / split / f"{num}__s{sample:02d}.py"


def manual_status(text: str) -> str:
    m = STATUS_RE.search(text)
    return m.group(1) if m else "TODO"


def manual_code(text: str) -> str:
    """The code part of a manual-cleaning file (everything after the header)."""
    return text.split(HEADER_END, 1)[1] if HEADER_END in text else text
