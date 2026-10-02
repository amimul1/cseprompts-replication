"""Create the two code-cleaning tracks for a generation run (coding tasks only).

    python scripts/prepare_cleaning.py --run results/generations/llama31_8b_instruct/greedy

MANUAL track (for you to clean by hand, as the paper did):
    annotations/manual_cleaning/<model>/<run>/<split>/NNN__sKK.py
  Each file starts with a comment header (task, prompt, instructions) and then the
  model's RAW response, unedited. Clean it following docs/MANUAL_CLEANING.md, then
  change the header line `# MANUAL_STATUS: TODO` to DONE (or NO_CODE).
  Existing files are NEVER overwritten, so re-running this is always safe.
  The files are committed to git: your cleaning is research data.

AUTOMATIC track (for comparison and side-by-side inspection):
    results/extracted/<model>/<run>/<split>/NNN__sKK.py
  Produced by cseprompts.harness.extract (deterministic; regenerated each run).

Also writes annotations/manual_cleaning/<model>/<run>/manifest.csv with a random
(seeded) order, so a spot-check of the first N rows is a fair random sample.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cseprompts.data import REPO_ROOT, load_coding  # noqa: E402
from cseprompts.harness.build import SUITE_DIR  # noqa: E402
from cseprompts.harness.extract import extract  # noqa: E402
from cseprompts.harness.runs import HEADER_END, load_run, manual_file, run_id  # noqa: E402

KIND_HINT = {
    "function": "FUNCTION task: keep the function/class definitions (and imports/helpers they need); "
                "remove example calls, prints and tests.",
    "custom": "CLASS/FUNCTION task: keep the definitions (and imports/helpers they need); remove example usage.",
    "program": "PROGRAM task: keep the whole program the model wrote (input, processing, printing).",
    "vars": "VARIABLES task: keep the whole script, including the variable assignments at the top.",
}


def header(uid: str, meta: dict, sample: int, kind: str, prompt: str) -> str:
    wrapped = []
    for para in prompt.strip().splitlines():
        wrapped += textwrap.wrap(para, 96) or [""]
    lines = [
        "# ================= CSEPrompts manual cleaning =================",
        f"# task: {uid} | model: {meta['model_key']} | run: {run_id(meta)[1]} | sample: {sample}",
        f"# {KIND_HINT.get(kind, '')}",
        "# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the",
        "# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it",
        "# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).",
        "# MANUAL_STATUS: TODO",
        "# ---- task prompt (reference only) ----",
        *[f"#   {ln}" for ln in wrapped],
        HEADER_END,
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", type=Path, required=True, help="a generation run directory")
    ap.add_argument("--samples", type=int, nargs="*", default=None,
                    help="which sample indices get manual files (default: all for greedy, only 0 otherwise)")
    args = ap.parse_args()

    run = load_run(args.run)
    meta = run["meta"]
    model_key, run_name = run_id(meta)
    kinds = {json.loads(l)["uid"]: json.loads(l)["kind"]
             for l in (SUITE_DIR / "original" / "tasks.jsonl").read_text().splitlines() if l.strip()}
    prompts = {p.uid: p.prompt for s in ("codingsites", "academic") for p in load_coding(s)}
    wanted = set(args.samples) if args.samples is not None else ({0} if meta["protocol"]["n"] > 1 else None)

    created = kept = 0
    rows = []
    for s in run["samples"]:
        if s["split"] == "mcq" or (wanted is not None and s["sample"] not in wanted):
            continue
        uid, k = s["uid"], s["sample"]
        kind = kinds[uid]
        auto = extract(s["completion"], kind)
        auto_path = REPO_ROOT / "results" / "extracted" / model_key / run_name / uid.split("/")[0] / \
            f"{uid.split('/')[1]}__s{k:02d}.py"
        auto_path.parent.mkdir(parents=True, exist_ok=True)
        auto_path.write_text(f"# auto-extracted ({auto.method}, extractor v{auto.version}); dropped: "
                             f"{len(auto.dropped)} top-level statements\n" + auto.code, encoding="utf-8")
        mpath = manual_file(model_key, run_name, uid, k)
        if mpath.exists():
            kept += 1
        else:
            mpath.parent.mkdir(parents=True, exist_ok=True)
            mpath.write_text(header(uid, meta, k, kind, prompts[uid]) + s["completion"] + "\n", encoding="utf-8")
            created += 1
        rows.append({"uid": uid, "sample": k, "kind": kind, "manual_file": str(mpath.relative_to(REPO_ROOT)),
                     "auto_file": str(auto_path.relative_to(REPO_ROOT)), "auto_method": auto.method,
                     "finish_reason": s.get("finish_reason")})

    random.Random(20260929).shuffle(rows)
    manifest = manual_file(model_key, run_name, "codingsites/001", 0).parents[1] / "manifest.csv"
    with manifest.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["order", *rows[0].keys()] if rows else ["order"])
        w.writeheader()
        for i, r in enumerate(rows, 1):
            w.writerow({"order": i, **r})
    print(f"manual files: {created} created, {kept} already existed (left untouched)")
    print(f"auto files:   {len(rows)} -> results/extracted/{model_key}/{run_name}/")
    print(f"manifest (random order for spot checks): {manifest.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
