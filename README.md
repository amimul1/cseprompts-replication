# CSEPrompts 2.0 — replication

A replication of **CSEPrompts 2.0** (Raihan et al., *On the performance of large language models on
introductory programming assignments*, Journal of Intelligent Information Systems 64:239–263, 2025)
with open-weight models, run on the GMU Hopper cluster.

The dataset is used **exactly as released** ([mraihan-gmu/CSEPrompts](https://github.com/mraihan-gmu/CSEPrompts)
@ `58d7ea0`, identical to the journal's supplementary material). Every expected value and MCQ key is
kept as released, because the paper graded with them.

## Results

pass@1 (%) on the released data, 95% bootstrap CI over tasks; the paper's value (read off its Fig. 3/4, ±2) in parentheses.

| Model | CodingSites | Academic | MCQ | code cleaning |
|---|---|---|---|---|
| meta-llama/Llama-3.1-8B-Instruct | 43.2 [34.7, 51.7] (40) | 37.0 [28.0, 46.0] (30) | 60.0 [50.0, 69.0] (52) | manual |
| mistralai/Mistral-7B-Instruct-v0.1 | 41.5 [32.2, 50.8] (44) | 25.0 [17.0, 34.0] (24) | pending (36) | *auto* (manual pending) |

Coding numbers marked *auto* use automatic code extraction; the final numbers use hand-cleaned code, as the paper did. Full reports: `results/replication/<model>/greedy/paper_replication.md`.

## What the paper did, and how this repo reproduces it

| Step | The paper | Here |
|---|---|---|
| Data | 118 coding-site + 101 MOOC prompts, 100 MCQs | `data/raw/CSEPrompts-main/` (unchanged) |
| Prompt | system prompt + task + instruction, zero-shot (Fig. 1–2) | same strings, system + user messages (`src/cseprompts/prompts.py`) |
| Models | LLaMA-3 8B (3.1), Mistral 7B (0.1), … | `meta-llama/Llama-3.1-8B-Instruct`, `mistralai/Mistral-7B-Instruct-v0.1`, pinned commits (`configs/models.json`) |
| Attempts | first attempt (pass@1) | one greedy answer, 2048 new tokens (`configs/protocols.json`) |
| Cleaning | responses "manually cleaned to isolate the code" | by hand, rules in `docs/MANUAL_CLEANING.md`; files in `annotations/manual_cleaning/` |
| Testing | pytest on the released test cases | the released prose tests converted to pytest, expected values unchanged (`data/processed/pytest/original/`) |
| Labels | 0 no code · 1 not executed · 2 all tests fail · 3 partial · 4 all pass | same (`src/cseprompts/harness/runner.py`) |
| MCQ | accuracy against the released keys, labels 0/1/2 | the option the model chose, graded against the released keys (`scripts/mcq.py`) |

The paper's own pytest files and cleaning rules were not released, so the conversion of the prose
tests and the cleaning rules are this repo's reconstruction. Academic #90 has no test cases in the
release, so Academic is scored on 100 tasks.

## Reproduce

Step-by-step commands (generation on a GPU cluster, manual cleaning, evaluation, MCQs, report):
**[docs/REPLICATION_PAPER.md](docs/REPLICATION_PAPER.md)**.

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest                       # unit tests, no GPU
.venv/bin/python scripts/paper_report.py --run results/generations/llama31_8b_instruct/greedy
```

Generation needs a GPU and vLLM (`requirements-gpu.txt`, `hopper/`). Model-written code is only run
through the sandboxed harness (`src/cseprompts/harness/`).

## Layout

```
data/raw/CSEPrompts-main/     the original release (AGPL-3.0, © its authors)
data/processed/pytest/original/  executable tests built from the released test cases
src/cseprompts/               prompts, provenance, harness (extraction, runner, metrics, MCQ grading)
scripts/                      generate, prepare_cleaning, evaluate, mcq, paper_report
hopper/                       Slurm jobs for GMU Hopper
annotations/                  hand-cleaned code and MCQ choices (research data)
results/generations/          raw model outputs (greedy)
results/replication/          paper-style reports
```

## Credit and license

All prompts, test cases and MCQs are from CSEPrompts by Nishat Raihan and co-authors; please cite
their paper. Code and data here are under the **AGPL-3.0**, the license of the original release.
Llama outputs were generated with Meta Llama 3.1 and are subject to the Llama 3.1 Community License
("Built with Llama").

Maintainer: Amimul Ehsan Zoha (George Mason University).
