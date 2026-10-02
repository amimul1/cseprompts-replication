"""Paper-style replication report for one greedy run: the CSEPrompts 2.0 setup, released data as-is.

    python scripts/paper_report.py --run results/generations/llama31_8b_instruct/greedy

Reads what the earlier steps wrote (nothing is re-run here):
  results/evaluations/<model>/<run>/manual/summary.json + samples.jsonl   (hand-cleaned code)
  results/evaluations/<model>/<run>/auto/summary.json + samples.jsonl     (automatic extraction, for comparison)
  results/evaluations/<model>/<run>/mcq_summary.json                      (scripts/mcq.py score)
Uses only the paper's view: ORIGINAL tests (released values, errors included), ALL tasks,
release MCQ keys. Writes results/replication/<model>/<run>/paper_replication.md and .json.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cseprompts.data import REPO_ROOT  # noqa: E402
from cseprompts.harness.runs import load_run, run_id  # noqa: E402

LABELS = ["NO_CODE", "NOT_EXECUTED", "ALL_FAILED", "PARTIAL", "ALL_PASSED"]
PAPER_COLUMNS = ["No Code Written", "Code not executed", "All test case failed",
                 "Partial Test cases passed", "All test cases passed"]  # Results/Comparison.csv
SPLITS = [("codingsites", "CodingSites"), ("academic", "Academic")]


def load_json(path: Path):
    return json.loads(path.read_text()) if path.exists() else None


def original_labels(path: Path) -> dict[str, int]:
    """task uid -> label (original mode, sample 0) from a samples.jsonl."""
    out = {}
    if path.exists():
        for line in path.read_text().splitlines():
            r = json.loads(line)
            if r["mode"] == "original" and r["sample"] == 0:
                out[r["uid"]] = r["label"]
    return out


def fmt_ci(m: dict) -> str:
    lo, hi = m["pass@1_ci95"]
    return f"{m['pass@1']:.1f} [{lo:.1f}, {hi:.1f}]"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", type=Path, required=True)
    args = ap.parse_args()
    meta = load_run(args.run)["meta"]
    model_key, run_name = run_id(meta)
    ev = REPO_ROOT / "results" / "evaluations" / model_key / run_name
    manual, auto = load_json(ev / "manual" / "summary.json"), load_json(ev / "auto" / "summary.json")
    mcq = load_json(ev / "mcq_summary.json")
    targets = json.loads((REPO_ROOT / "configs" / "paper_targets.json").read_text())
    row = targets["model_to_row"].get(model_key)
    paper = targets["rows"].get(row, {}) if row else {}

    warnings = []
    if manual is None:
        warnings.append("No manual-track evaluation yet (step 4 of docs/REPLICATION_PAPER.md).")
    elif manual["coverage"].get("todo") or manual["coverage"].get("missing"):
        warnings.append(f"Manual cleaning incomplete: {manual['coverage']}.")
    if mcq is None:
        warnings.append("No MCQ score yet (step 5).")
    elif mcq["human_checked"] < mcq["rows"]:
        warnings.append(f"MCQ: only {mcq['human_checked']}/{mcq['rows']} rows human-checked; the rest use the "
                        "automatic suggestion.")

    main_track = manual or auto
    track_name = "manual" if manual else "auto (manual not available yet)"
    result = {"model_key": model_key, "run": run_name, "hf_id": meta.get("hf_id"), "revision": meta.get("revision"),
              "paper_row": row, "track": track_name, "warnings": warnings, "coding": {}, "mcq": None,
              "manual_vs_auto": None}

    md = [f"# Replication of CSEPrompts 2.0: {model_key} ({run_name})", "",
          "Setup as in the paper: released data **as is** (no corrections), paper prompt (system + task + "
          "instruction), one zero-shot attempt (greedy), code cleaned by hand, graded by the released test "
          "cases with the paper's 0–4 rubric (Guidelines.csv), MCQs graded against the released keys.", "",
          f"- Model: `{meta.get('hf_id')}` @ `{meta.get('revision')}`; paper row: {row}",
          f"- Coding results from the **{track_name}** cleaning track; 95% bootstrap CIs over tasks.", ""]
    if warnings:
        md += ["> **Not final:**", *[f"> - {w}" for w in warnings], ""]

    md += ["## pass@1 (%)", "", "| | ours [95% CI] | paper (±2, read off Fig. 3/4) | paper inside our CI? |",
           "|---|---|---|---|"]
    for key, name in SPLITS:
        if main_track:
            m = main_track["metrics"][f"original/{key}/all"]
            lo, hi = m["pass@1_ci95"]
            p = paper.get(key)
            inside = "—" if p is None else ("yes" if lo <= p <= hi else "no")
            md.append(f"| {name} (n={m['n_tasks']}) | {fmt_ci(m)} | {p if p is not None else '—'} | {inside} |")
            result["coding"][key] = {"pass@1": m["pass@1"], "ci95": m["pass@1_ci95"], "n_tasks": m["n_tasks"],
                                     "labels_pct": m["labels_pct"], "paper": p}
    if mcq:
        m = mcq["release"]
        lo, hi = m["ci95"]
        p = paper.get("mcq")
        inside = "—" if p is None else ("yes" if lo <= p <= hi else "no")
        md.append(f"| MCQ accuracy (n={m['n_items']}) | {m['accuracy']:.1f} [{lo:.1f}, {hi:.1f}] | "
                  f"{p if p is not None else '—'} | {inside} |")
        result["mcq"] = {**m, "paper": p, "human_checked": mcq["human_checked"], "rows": mcq["rows"]}
    md.append("")

    if main_track:
        md += ["## Label distribution (% of tasks), in the format of the release's `Results/Comparison.csv`", "",
               "| Platform | " + " | ".join(PAPER_COLUMNS) + " |", "|---|" + "---|" * len(PAPER_COLUMNS)]
        for key, name in SPLITS:
            pct = main_track["metrics"][f"original/{key}/all"]["labels_pct"]
            md.append(f"| {name} | " + " | ".join(f"{pct[l]:.2f}" for l in LABELS) + " |")
        md.append("")
    if mcq:
        lp = mcq["release"]["labels_pct"]
        md += ["## MCQ labels (% of responses; paper rubric)", "", "| Incorrect (0) | Partially correct (1) | Correct (2) |",
               "|---|---|---|", f"| {lp['0']:.1f} | {lp['1']:.1f} | {lp['2']:.1f} |", ""]

    if manual and auto:
        man = original_labels(ev / "manual" / "samples.jsonl")
        aut = original_labels(ev / "auto" / "samples.jsonl")
        common = sorted(set(man) & set(aut))
        same = sum(man[u] == aut[u] for u in common)
        diff = [u for u in common if man[u] != aut[u]]
        result["manual_vs_auto"] = {"tasks": len(common), "same_label": same, "different": diff}
        md += ["## Manual vs automatic cleaning", "",
               f"Same label on {same}/{len(common)} tasks ({100 * same / max(len(common), 1):.1f}%). "
               "Automatic-track pass@1: " + ", ".join(
                   f"{name} {auto['metrics'][f'original/{key}/all']['pass@1']:.1f}" for key, name in SPLITS) + ".",
               "", "Tasks whose label differs: " + (", ".join(diff) if diff else "none") + ".", ""]

    md += ["## Caveats", "",
           "- The release has prose test cases, not the paper's pytest files. We converted each to an executable "
           "test without changing any expected value (`data/processed/pytest/original/`); this is the closest "
           "available reconstruction of the paper's grading.",
           "- The paper's numbers are read off its bar charts (±2 points).",
           "- Academic/090 has no released tests (its test field holds a test-writing instruction), so Academic "
           "is scored on 100 tasks, not 101.",
           "- Released expected values and MCQ keys are kept even where they disagree with the prompt or with "
           "what Python does, because the paper graded with them.", ""]

    out = REPO_ROOT / "results" / "replication" / model_key / run_name
    out.mkdir(parents=True, exist_ok=True)
    (out / "paper_replication.json").write_text(json.dumps(result, indent=2))
    (out / "paper_replication.md").write_text("\n".join(md))
    print("\n".join(md))
    print(f"-> {(out / 'paper_replication.md').relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
