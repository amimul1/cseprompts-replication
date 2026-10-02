"""Generate model outputs for CSEPrompts prompts.

Research runs use a registered model (configs/models.json, pinned revision) and a
named decoding protocol (configs/protocols.json):

    python scripts/generate.py --model-key llama31_8b_instruct --protocol greedy
    python scripts/generate.py --model-key mistral_7b_instruct_v01 --protocol sampled

Ad hoc / smoke runs can name any HF model directly:

    python scripts/generate.py --model Qwen/Qwen2.5-Coder-0.5B-Instruct --protocol greedy --limit 5
    python scripts/generate.py --backend mock --model mock --protocol greedy --limit 3   # Mac dry run

Output (write-once; refuses to overwrite an existing run unless --overwrite):
    <out-dir>/<model-key>/<protocol>[__limitN]/
        prompts.jsonl        one line per prompt: uid, split, prompt_mode, rendered_prompt, prompt_tokens
        <split>.jsonl        one line per sample: uid, split, sample, completion, finish_reason, completion_tokens
        run_meta.json        model + revision, protocol, exact SamplingParams, counts, timing, provenance
<out-dir> defaults to $CSE_STORE/results/generations on Hopper, else <repo>/results/generations.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cseprompts import config, provenance  # noqa: E402
from cseprompts.data import REPO_ROOT, load_coding, load_mcq  # noqa: E402
from cseprompts.prompts import flatten, paper_messages, render  # noqa: E402

SPLITS = ("codingsites", "academic", "mcq")


def default_out_dir() -> Path:
    store = os.environ.get("CSE_STORE")
    return Path(store) / "results" / "generations" if store else REPO_ROOT / "results" / "generations"


def build_items(split: str, limit: int | None) -> list[dict]:
    if split == "mcq":
        items = [{"uid": q.uid, "split": split, "messages": paper_messages(q.prompt, "mcq")} for q in load_mcq()]
    else:
        items = [{"uid": p.uid, "split": split, "messages": paper_messages(p.prompt, "code")} for p in load_coding(split)]
    return items[:limit] if limit else items


def resolve_revision(hf_id: str, revision: str | None) -> str | None:
    """Pinned revision from the registry, else ask the Hub for the current commit (recorded, then used)."""
    if revision:
        return revision
    try:
        from huggingface_hub import model_info

        return model_info(hf_id).sha
    except Exception as exc:  # offline, gated without login, etc.
        print(f"warning: could not resolve a revision for {hf_id}: {exc}", flush=True)
        return None


def generate_mock(items, proto, prompt_mode):
    prompts = [{"prompt_mode": "plain", "rendered_prompt": flatten(it["messages"]), "prompt_tokens": None} for it in items]
    samples = [
        [{"completion": f"```python\n# mock completion {k}\nprint('hello')\n```", "finish_reason": "stop",
          "completion_tokens": None} for k in range(proto["n"])]
        for _ in items
    ]
    return prompts, samples, "mock"


def generate_vllm(items, proto, prompt_mode, hf_id, revision, tp, max_model_len, gpu_mem):
    from vllm import LLM, SamplingParams

    llm = LLM(
        model=hf_id,
        revision=revision,
        tokenizer_revision=revision,
        tensor_parallel_size=tp,
        max_model_len=max_model_len,
        gpu_memory_utilization=gpu_mem,
        seed=proto["seed"],
        trust_remote_code=False,
    )
    tokenizer = llm.get_tokenizer()
    rendered = [render(it["messages"], tokenizer, prompt_mode) for it in items]
    params = SamplingParams(
        n=proto["n"], temperature=proto["temperature"], top_p=proto["top_p"],
        max_tokens=proto["max_tokens"], seed=proto["seed"],
    )
    outputs = llm.generate([text for text, _ in rendered], params, use_tqdm=True)
    prompts = [
        {"prompt_mode": mode, "rendered_prompt": text, "prompt_tokens": len(out.prompt_token_ids or [])}
        for (text, mode), out in zip(rendered, outputs)
    ]
    samples = [
        [{"completion": o.text, "finish_reason": o.finish_reason, "completion_tokens": len(o.token_ids)}
         for o in out.outputs]
        for out in outputs
    ]
    return prompts, samples, repr(params)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    who = ap.add_mutually_exclusive_group(required=True)
    who.add_argument("--model-key", help="registered model (configs/models.json)")
    who.add_argument("--model", help="ad hoc Hugging Face id, or 'mock' with --backend mock")
    ap.add_argument("--protocol", required=True, help="decoding protocol (configs/protocols.json)")
    ap.add_argument("--backend", choices=["vllm", "mock"], default="vllm")
    ap.add_argument("--splits", nargs="+", choices=SPLITS, default=list(SPLITS))
    ap.add_argument("--limit", type=int, default=None, help="only the first N prompts per split (smoke tests)")
    ap.add_argument("--prompt-mode", choices=["auto", "chat-system", "chat-user", "plain"], default=None,
                    help="override the registry's prompt mode (see cseprompts.prompts.render)")
    ap.add_argument("--tp", type=int, default=1, help="tensor-parallel size = number of GPUs")
    ap.add_argument("--max-model-len", type=int, default=4096)
    ap.add_argument("--gpu-mem", type=float, default=0.85, help="fraction of GPU memory vLLM may use")
    ap.add_argument("--out-dir", type=Path, default=None)
    ap.add_argument("--overwrite", action="store_true", help="replace an existing run (raw outputs are write-once by default)")
    args = ap.parse_args()

    proto = config.protocol(args.protocol)
    if args.model_key:
        entry = config.model(args.model_key)
        key, hf_id, revision = args.model_key, entry["hf_id"], entry["revision"]
        prompt_mode = args.prompt_mode or entry.get("prompt_mode", "auto")
    else:
        entry = None
        key, hf_id = args.model.replace("/", "__"), args.model
        revision = None if args.backend == "mock" else resolve_revision(hf_id, None)
        prompt_mode = args.prompt_mode or "auto"

    run_name = args.protocol + (f"__limit{args.limit}" if args.limit else "")
    run_dir = (args.out_dir or default_out_dir()) / key / run_name
    if (run_dir / "run_meta.json").exists() and not args.overwrite:
        raise SystemExit(f"{run_dir} already has a finished run; refusing to overwrite raw outputs (use --overwrite).")
    run_dir.mkdir(parents=True, exist_ok=True)

    items = [it for s in args.splits for it in build_items(s, args.limit)]
    print(f"{len(items)} prompts x {proto['n']} samples | model={hf_id} @ {revision} | protocol={args.protocol} "
          f"| backend={args.backend}", flush=True)

    start = time.time()
    if args.backend == "mock":
        prompts, samples, params_repr = generate_mock(items, proto, prompt_mode)
    else:
        prompts, samples, params_repr = generate_vllm(
            items, proto, prompt_mode, hf_id, revision, args.tp, args.max_model_len, args.gpu_mem)
    elapsed = time.time() - start

    with (run_dir / "prompts.jsonl").open("w", encoding="utf-8") as f:
        for it, p in zip(items, prompts):
            f.write(json.dumps({"uid": it["uid"], "split": it["split"], **p}) + "\n")
    files = {s: (run_dir / f"{s}.jsonl").open("w", encoding="utf-8") for s in args.splits}
    finish = Counter()
    for it, per_item in zip(items, samples):
        for k, s in enumerate(per_item):
            finish[s["finish_reason"]] += 1
            files[it["split"]].write(json.dumps({"uid": it["uid"], "split": it["split"], "sample": k, **s}) + "\n")
    for f in files.values():
        f.close()

    modes = Counter(p["prompt_mode"] for p in prompts)
    meta = {
        "model_key": key,
        "hf_id": hf_id,
        "revision": revision,
        "registry_entry": entry,
        "protocol_name": args.protocol,
        "protocol": proto,
        "sampling_params": params_repr,
        "prompt_mode_requested": prompt_mode,
        "prompt_modes_used": dict(modes),
        "splits": args.splits,
        "limit": args.limit,
        "n_prompts": dict(Counter(it["split"] for it in items)),
        "n_samples_total": sum(len(s) for s in samples),
        "finish_reasons": dict(finish),
        "backend": args.backend,
        "engine": {"tp": args.tp, "max_model_len": args.max_model_len, "gpu_mem": args.gpu_mem},
        "seconds": round(elapsed, 1),
        "provenance": provenance.collect(),
    }
    (run_dir / "run_meta.json").write_text(json.dumps(meta, indent=2))
    print(f"prompt modes used: {dict(modes)} | finish reasons: {dict(finish)}", flush=True)
    print(f"done in {elapsed:.1f}s -> {run_dir}")


if __name__ == "__main__":
    main()
