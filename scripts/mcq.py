"""MCQ annotation sheet and scoring for a generation run.

    python scripts/mcq.py sheet --run results/generations/llama31_8b_instruct/greedy
    python scripts/mcq.py score --run results/generations/llama31_8b_instruct/greedy

sheet: writes annotations/mcq/<model>/<run>.csv (never overwrites an existing sheet).
       One row per MCQ response. `options` lists the options as [0] ... || [1] ...; fill the
       `chosen` column with the NUMBER(S) of the option(s) the model picked (e.g. `3` or `3, 5`);
       leave `chosen` empty for no answer. Numbers, not text: some options differ only in
       indentation. `auto_chosen` is a heuristic suggestion; set `checked` to 1 on each row you
       have verified.
score: grades every row (rows with checked=1 use `chosen`, others use `auto_chosen`) against
       the release keys (100 items) and the validated keys (58 scorable distinct items,
       data/curation/mcq.py), with the paper's 0/1/2 rubric;
       writes results/evaluations/<model>/<run>/mcq_summary.json/.md
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cseprompts.data import REPO_ROOT  # noqa: E402
from cseprompts.harness.mcq import auto_choice, choice_numbers, grade, has_validated_keys, items  # noqa: E402
from cseprompts.harness.metrics import bootstrap_ci, mean  # noqa: E402
from cseprompts.harness.runs import load_run, run_id  # noqa: E402

SEP = " || "
MODES = ("release", "validated") if has_validated_keys() else ("release",)


def sheet_path(meta) -> Path:
    key, run_name = run_id(meta)
    return REPO_ROOT / "annotations" / "mcq" / key / f"{run_name}.csv"


def make_sheet(run) -> None:
    path = sheet_path(run["meta"])
    if path.exists():
        print(f"{path.relative_to(REPO_ROOT)} exists; not overwritten")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    by_uid = {i["uid"]: i for i in items("release")}
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["uid", "sample", "options", "auto_chosen", "chosen", "checked",
                                          "question", "response"])
        w.writeheader()
        for s in run["samples"]:
            if s["split"] != "mcq":
                continue
            q = by_uid[s["uid"]]
            opts = q["options"]
            auto = choice_numbers(auto_choice(s["completion"], opts), opts)
            w.writerow({"uid": s["uid"], "sample": s["sample"],
                        "options": SEP.join(f"[{i}] {o}" for i, o in enumerate(opts)),
                        "auto_chosen": ", ".join(map(str, auto)), "chosen": "", "checked": "",
                        "question": q["prompt"], "response": s["completion"]})
    print(f"sheet -> {path.relative_to(REPO_ROOT)}")


def score(run) -> None:
    path = sheet_path(run["meta"])
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    n_checked = sum(1 for r in rows if r["checked"].strip() == "1")
    out = {"sheet": str(path.relative_to(REPO_ROOT)), "rows": len(rows), "human_checked": n_checked}
    for mode in MODES:
        keys = {i["uid"]: i["accept"] for i in items(mode)}
        per_item, labels = {}, {0: 0, 1: 0, 2: 0}
        for r in rows:
            if r["uid"] not in keys:
                continue
            chosen = r["chosen"] if r["checked"].strip() == "1" else r["auto_chosen"]
            lab = grade([int(n) for n in re.findall(r"\d+", chosen)], keys[r["uid"]])
            per_item.setdefault(r["uid"], []).append(1.0 if lab == 2 else 0.0)
            labels[lab] += 1
        acc = [mean(v) for v in per_item.values()]
        lo, hi = bootstrap_ci(acc)
        total = sum(labels.values()) or 1
        out[mode] = {"n_items": len(per_item), "accuracy": 100 * mean(acc), "ci95": [100 * lo, 100 * hi],
                     "labels_pct": {str(k): 100 * v / total for k, v in labels.items()}}
    key, run_name = run_id(run["meta"])
    d = REPO_ROOT / "results" / "evaluations" / key / run_name
    d.mkdir(parents=True, exist_ok=True)
    (d / "mcq_summary.json").write_text(json.dumps(out, indent=2))
    md = [f"# MCQ — {key} — {run_name}", "",
          f"Human-checked rows: {n_checked}/{len(rows)} (unchecked rows use the automatic suggestion)", "",
          "| keys | items | accuracy % (label 2) [95% CI] | label 0 / 1 / 2 (%) |", "|---|---|---|---|"]
    for mode in MODES:
        m = out[mode]
        md.append(f"| {mode} | {m['n_items']} | {m['accuracy']:.1f} [{m['ci95'][0]:.1f}, {m['ci95'][1]:.1f}] | "
                  + " / ".join(f"{m['labels_pct'][k]:.1f}" for k in ("0", "1", "2")) + " |")
    (d / "mcq_summary.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", choices=["sheet", "score"])
    ap.add_argument("--run", type=Path, required=True)
    args = ap.parse_args()
    run = load_run(args.run)
    make_sheet(run) if args.action == "sheet" else score(run)


if __name__ == "__main__":
    main()
