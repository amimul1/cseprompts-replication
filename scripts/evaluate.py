"""Evaluate a generation run on the coding tasks.

    python scripts/evaluate.py --run results/generations/llama31_8b_instruct/greedy --track auto
    python scripts/evaluate.py --run results/generations/llama31_8b_instruct/greedy --track manual

Tracks:
  auto     code extracted automatically from each response (cseprompts.harness.extract)
  manual   your hand-cleaned files (annotations/manual_cleaning/...); only files marked
           DONE or NO_CODE are scored, and the summary reports how many are still TODO
Modes (both by default):
  original   the released tests, mechanically converted (paper-comparable)
  validated  corrected tests on well-posed tasks (a later benchmark version; optional)

Writes results/evaluations/<model>/<run>/<track>/
  samples.jsonl   one row per (sample, mode): label 0-4, tests passed, error types, entry used ...
  summary.json    all metrics
  summary.md      the tables to report (pass@1 with 95% CI, label distribution, errors, paper targets)

RUN THIS ON HOPPER (CPU job hopper/jobs/20_evaluate.sbatch) for full runs: it executes model-written code.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cseprompts import provenance  # noqa: E402
from cseprompts.data import REPO_ROOT  # noqa: E402
from cseprompts.harness.build import MODES, SUITE_DIR  # noqa: E402
from cseprompts.harness.extract import EXTRACTOR_VERSION, extract  # noqa: E402
from cseprompts.harness.metrics import bootstrap_ci, mean, pass_at_k  # noqa: E402
from cseprompts.harness.runner import LABELS, evaluate  # noqa: E402
from cseprompts.harness.runs import load_run, manual_code, manual_file, manual_status, run_id  # noqa: E402

SPLITS = ("codingsites", "academic")


AVAILABLE_MODES = [m for m in MODES if (SUITE_DIR / m / "tasks.jsonl").exists()]  # a repo may ship only `original`


def manifests() -> dict:
    out = {}
    for mode in AVAILABLE_MODES:
        rows = [json.loads(l) for l in (SUITE_DIR / mode / "tasks.jsonl").read_text().splitlines() if l.strip()]
        out[mode] = {r["uid"]: r for r in rows}
    return out


def summarize(rows: list[dict], man: dict, n_samples: int) -> dict:
    """Metrics per mode x split x subset (all tasks with tests / well-posed tasks only)."""
    summary = {}
    by = defaultdict(list)
    for r in rows:
        by[(r["mode"], r["uid"])].append(r)
    for mode in MODES:
        for split in (*SPLITS, "all"):
            for subset in ("all", "well_posed"):
                tasks = [uid for (m, uid) in by if m == mode and (split == "all" or uid.startswith(split))
                         and (subset == "all" or man[mode][uid]["well_posed"])]
                if not tasks:
                    continue
                per_task_p1, labels, errors = [], Counter(), Counter()
                ks = [k for k in (1, 5, 10) if k <= n_samples]
                pk = {k: [] for k in ks}
                for uid in tasks:
                    rs = by[(mode, uid)]
                    n = len(rs)
                    c = sum(1 for r in rs if r["label"] == 4)
                    for k in ks:
                        pk[k].append(pass_at_k(n, c, k))
                    per_task_p1.append(pass_at_k(n, c, 1))
                    labels.update(r["label_name"] for r in rs)
                    for r in rs:
                        if r.get("load_error"):
                            errors[r["load_error"]] += 1
                        for t in (r.get("tests") or {}).values():
                            if t.get("outcome") != "passed" and t.get("error"):
                                errors[t["error"]] += 1
                total = sum(labels.values())
                lo, hi = bootstrap_ci(per_task_p1)
                summary[f"{mode}/{split}/{subset}"] = {
                    "mode": mode, "split": split, "subset": subset, "n_tasks": len(tasks), "n_samples": total,
                    "pass@1": 100 * mean(per_task_p1), "pass@1_ci95": [100 * lo, 100 * hi],
                    **{f"pass@{k}": 100 * mean(v) for k, v in pk.items() if k > 1},
                    "labels_pct": {LABELS[i]: 100 * labels.get(LABELS[i], 0) / total for i in range(5)},
                    "errors": dict(errors.most_common()),
                }
    return summary


def to_markdown(summary: dict, meta: dict, track: str, coverage: dict, targets: dict) -> str:
    key, run_name = run_id(meta)
    row = targets["model_to_row"].get(key)
    paper = targets["rows"].get(row, {}) if row else {}
    lines = [f"# {key} — {run_name} — {track} cleaning", "",
             f"- Model: `{meta['hf_id']}` @ `{meta['revision']}`",
             f"- Protocol: `{meta['protocol_name']}` {meta['protocol']}",
             f"- Samples per task: {meta['protocol']['n']}; extractor v{EXTRACTOR_VERSION}; "
             f"coverage: {coverage}", ""]
    lines += ["## pass@1 (%) with 95% bootstrap CI over tasks", "",
              "| mode | tasks | CodingSites | Academic | All | paper (CodingSites / Academic) |", "|---|---|---|---|---|---|"]
    for mode in MODES:
        if not any(k.startswith(f"{mode}/") for k in summary):
            continue
        for subset in ("all", "well_posed"):
            cells = []
            n_tasks = None
            for split in (*SPLITS, "all"):
                s = summary.get(f"{mode}/{split}/{subset}")
                if s:
                    cells.append(f"{s['pass@1']:.1f} [{s['pass@1_ci95'][0]:.1f}, {s['pass@1_ci95'][1]:.1f}] (n={s['n_tasks']})")
                    n_tasks = s["n_tasks"] if split == "all" else n_tasks
                else:
                    cells.append("—")
            ref = f"{paper.get('codingsites', '—')} / {paper.get('academic', '—')} ({row})" if (paper and mode == "original" and subset == "all") else ""
            lines.append(f"| {mode} | {subset.replace('_', '-')} | {' | '.join(cells)} | {ref} |")
    lines += ["", "## Label distribution (% of samples), paper rubric", "",
              "| mode / split (all tasks) | " + " | ".join(LABELS[i] for i in range(5)) + " |",
              "|---|" + "---|" * 5]
    for mode in MODES:
        for split in SPLITS:
            s = summary.get(f"{mode}/{split}/all")
            if s:
                lines.append(f"| {mode} / {split} | " + " | ".join(f"{s['labels_pct'][LABELS[i]]:.1f}" for i in range(5)) + " |")
    s = summary.get("original/all/all")
    if s and s["errors"]:
        lines += ["", "## Error types (original tests, all tasks; counts over failing tests and load errors)", ""]
        lines += [f"- {k}: {v}" for k, v in list(s["errors"].items())[:15]]
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", type=Path, required=True)
    ap.add_argument("--track", choices=["auto", "manual"], required=True)
    ap.add_argument("--modes", nargs="+", choices=AVAILABLE_MODES, default=AVAILABLE_MODES)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out", type=Path, default=REPO_ROOT / "results" / "evaluations")
    args = ap.parse_args()

    run = load_run(args.run)
    meta = run["meta"]
    model_key, run_name = run_id(meta)
    man = manifests()
    coverage = Counter()
    jobs = []
    for s in run["samples"]:
        if s["split"] not in SPLITS:
            continue
        uid, k = s["uid"], s["sample"]
        kind = man["original"][uid]["kind"]
        extra = {}
        if args.track == "auto":
            ex = extract(s["completion"], kind)
            code, extra = ex.code, {"extraction": ex.method, "extraction_dropped": len(ex.dropped)}
            coverage["scored"] += 1
        else:
            path = manual_file(model_key, run_name, uid, k)
            if not path.exists():
                coverage["missing"] += 1
                continue
            text = path.read_text(encoding="utf-8")
            status = manual_status(text)
            if status == "TODO":
                coverage["todo"] += 1
                continue
            code = "" if status == "NO_CODE" else manual_code(text)
            coverage["scored"] += 1
        for mode in args.modes:
            t = man[mode][uid]
            if t["n_tests"] == 0:
                continue
            jobs.append((uid, k, mode, kind, code, SUITE_DIR / mode / t["test_file"],
                         {**extra, "finish_reason": s.get("finish_reason")}))

    def work(job):
        uid, k, mode, kind, code, test_file, extra = job
        res = evaluate(code, test_file, kind)
        return {"uid": uid, "sample": k, "mode": mode, **extra, **res}

    t0 = time.time()
    with ThreadPoolExecutor(args.workers) as pool:
        rows = list(pool.map(work, jobs))
    out_dir = args.out / model_key / run_name / args.track
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "samples.jsonl").open("w") as f:
        for r in rows:
            f.write(json.dumps(r, default=str) + "\n")
    summary = summarize(rows, man, meta["protocol"]["n"])
    targets = json.loads((REPO_ROOT / "configs" / "paper_targets.json").read_text())
    full = {"run": {k: meta[k] for k in ("model_key", "hf_id", "revision", "protocol_name", "protocol")},
            "track": args.track, "extractor_version": EXTRACTOR_VERSION, "coverage": dict(coverage),
            "seconds": round(time.time() - t0, 1), "metrics": summary, "provenance": provenance.collect()}
    (out_dir / "summary.json").write_text(json.dumps(full, indent=2, default=str))
    md = to_markdown(summary, meta, args.track, dict(coverage), targets)
    (out_dir / "summary.md").write_text(md)
    print(md)
    print(f"-> {out_dir}  ({len(rows)} evaluations in {time.time() - t0:.0f}s)")


if __name__ == "__main__":
    main()
