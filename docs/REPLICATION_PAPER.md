# Replicating CSEPrompts 2.0 exactly as the paper did (released data as-is)

Goal: reproduce the paper's numbers for one model with the **released dataset unchanged**: every
prompt, expected value and MCQ key exactly as released, including duplicates and any values that
disagree with their prompt. Corrections belong to a later benchmark version (`validated` mode); nothing
in this procedure uses them.

Start with Llama (`llama31_8b_instruct`); repeat with `mistral_7b_instruct_v01` by swapping the key.

## What the paper did, and how each step is reproduced

| # | The paper (Raihan et al., JIIS 2025, §3–4) | This replication | Where |
|---|---|---|---|
| 1 | 219 coding prompts + 100 MCQs from the public release | The release, byte-identical to GitHub 58d7ea0 and the journal supplement | `data/raw/` (never edited) |
| 2 | Prompt = system prompt + task + instruction (Fig. 1–2), zero-shot | Same strings, sent as system + user messages | `src/cseprompts/prompts.py` |
| 3 | LLaMA-3, 8B, "3.1" | `meta-llama/Llama-3.1-8B-Instruct`, pinned commit | `configs/models.json` |
| 4 | One answer per prompt ("first attempt") | One greedy answer, 2048 new tokens | `configs/protocols.json` (`greedy`) |
| 5 | Responses "manually cleaned to isolate the code" | You clean every response by hand | `docs/MANUAL_CLEANING.md` |
| 6 | Code run with pytest on the released test cases (≥5 per prompt) | The released prose tests, converted to pytest **with every released expected value kept**, errors included | `data/processed/pytest/original/` |
| 7 | Label 0–4 per response (Guidelines.csv); pass@1 = share with label 4 | Same labels and metric, plus a 95% CI | `scripts/evaluate.py` |
| 8 | MCQ accuracy, labels 0/1/2, against the released keys | You record the option the model chose; graded against the released keys | `scripts/mcq.py` (release mode) |

What cannot be exactly the same: the paper's pytest files, cleaning rules and annotators were not
released. Steps 5–6 are therefore the closest reconstruction, and the report states this.

## Commands

Hopper commands start, every login, with:

```bash
cd ~/CSEPROMPTS && source hopper/env.sh && git pull
```

### Step 1. Generate (Hopper, GPU) — already done for Llama and Mistral

Done on 2026-09-29: job 1395330 (Llama greedy) and job 1395319 (Mistral greedy). The outputs are
in `/scratch/<netid>/cseprompts/results/generations/<model>/greedy/` and on the Mac under
`results/generations/`. To redo it from scratch (not needed):

```bash
sbatch --export=ALL,MODEL_KEY=llama31_8b_instruct,PROTOCOL=greedy hopper/jobs/10_generate.sbatch
```

### Step 2. Create the cleaning files (Mac)

```bash
cd ~/Desktop/CSEPROMPTS
.venv/bin/python scripts/prepare_cleaning.py --run results/generations/llama31_8b_instruct/greedy
```

This writes 219 files: `annotations/manual_cleaning/llama31_8b_instruct/greedy/<split>/NNN__s00.py`.
Each file contains the model's raw response.

### Step 3. Clean by hand (Mac) — about 2 hours

Open the folder in VS Code:

```bash
open -a "Visual Studio Code" annotations/manual_cleaning/llama31_8b_instruct/greedy
```

For each file (follow `docs/MANUAL_CLEANING.md`):
1. Below the line `# ---- model response below: edit from here ----`, delete everything that is not
   the model's code: prose, ``` fences, example output, and (for function tasks) example calls.
2. Never fix the code: no bug fixes, renames or added imports.
3. Change `# MANUAL_STATUS: TODO` to `DONE`, or to `NO_CODE` if the response has no Python code.

Commit after each session so nothing is lost:

```bash
git add annotations && git commit -m "Manual cleaning: Llama greedy (progress)" && git push
```

Check how many are left:

```bash
grep -rl "MANUAL_STATUS: TODO" annotations/manual_cleaning/llama31_8b_instruct/greedy | wc -l
```

### Step 4. Run the cleaned code on the released tests (Hopper, CPU job)

The cleaned files are model-written code, so they run on Hopper, not on the Mac. After pushing step 3:

```bash
cd ~/CSEPROMPTS && source hopper/env.sh && git pull
sbatch --export=ALL,MODEL_KEY=llama31_8b_instruct,PROTOCOL=greedy,TRACK=manual,MODES=original hopper/jobs/20_evaluate.sbatch
```

`MODES=original` = the released tests only, errors included. When `squeue -u $USER` is empty, copy
the results to the Mac (Mac terminal):

```bash
rsync -av <netid>@hopper.orc.gmu.edu:/scratch/<netid>/cseprompts/results/evaluations/ ~/Desktop/CSEPROMPTS/results/evaluations/
```

### Step 5. MCQs (Mac) — about 45 minutes

```bash
.venv/bin/python scripts/mcq.py sheet --run results/generations/llama31_8b_instruct/greedy
```

Open `annotations/mcq/llama31_8b_instruct/greedy.csv` (Excel or VS Code). For each of the 100 rows:
1. Read `response` and decide which option the model chose.
2. Write its **number** in `chosen`. The `options` column lists them as `[0] … || [1] …`. If the model
   picked several options, write e.g. `2, 5`; if it gave no answer, leave `chosen` empty.
3. Set `checked` to `1`.

`auto_chosen` is only a suggestion, so check it. Then score:

```bash
.venv/bin/python scripts/mcq.py score --run results/generations/llama31_8b_instruct/greedy
```

The paper's number is the `release` row (all 100 items, released keys). The `validated` row is for
the new benchmark, not for this replication.

### Step 6. The replication report (Mac)

```bash
.venv/bin/python scripts/paper_report.py --run results/generations/llama31_8b_instruct/greedy
```

This writes `results/replication/llama31_8b_instruct/greedy/paper_replication.md`:
- pass@1 for CodingSites, Academic and MCQ next to the paper's numbers, with "paper inside our CI?";
- the label distribution in the format of the release's `Results/Comparison.csv`;
- MCQ labels 0/1/2;
- agreement between your manual cleaning and the automatic extractor.

Commit everything:

```bash
git add annotations results && git commit -m "Paper replication: Llama-3.1-8B (manual track, released data)" && git push
```

## How to read the result

- **Replicated:** the paper's value lies inside our 95% CI for CodingSites, Academic and MCQ.
- The automatic track already puts both coding numbers inside the CI (43.2 vs 40; 37.0 vs 30).
  The manual track is what the paper did, so it is the number to report.
- Large differences between manual and automatic cleaning point to responses whose code is hard to
  isolate. List them in the report; they are where the two ways of cleaning disagree.
