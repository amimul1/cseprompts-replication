# Replication of CSEPrompts 2.0: mistral_7b_instruct_v01 (greedy)

Setup as in the paper: released data **as is** (no corrections), paper prompt (system + task + instruction), one zero-shot attempt (greedy), code cleaned by hand, graded by the released test cases with the paper's 0–4 rubric (Guidelines.csv), MCQs graded against the released keys.

- Model: `mistralai/Mistral-7B-Instruct-v0.1` @ `ec5deb64f2c6e6fa90c1abf74a91d5c93a9669ca`; paper row: Mistral
- Coding results from the **auto (manual not available yet)** cleaning track; 95% bootstrap CIs over tasks.

> **Not final:**
> - No manual-track evaluation yet (step 4 of docs/REPLICATION_PAPER.md).
> - No MCQ score yet (step 5).

## pass@1 (%)

| | ours [95% CI] | paper (±2, read off Fig. 3/4) | paper inside our CI? |
|---|---|---|---|
| CodingSites (n=118) | 41.5 [32.2, 50.8] | 44 | yes |
| Academic (n=100) | 25.0 [17.0, 34.0] | 24 | yes |

## Label distribution (% of tasks), in the format of the release's `Results/Comparison.csv`

| Platform | No Code Written | Code not executed | All test case failed | Partial Test cases passed | All test cases passed |
|---|---|---|---|---|---|
| CodingSites | 0.00 | 16.10 | 18.64 | 23.73 | 41.53 |
| Academic | 0.00 | 12.00 | 27.00 | 36.00 | 25.00 |

## Caveats

- The release has prose test cases, not the paper's pytest files. We converted each to an executable test without changing any expected value (`data/processed/pytest/original/`); this is the closest available reconstruction of the paper's grading.
- The paper's numbers are read off its bar charts (±2 points).
- Academic/090 has no released tests (its test field holds a test-writing instruction), so Academic is scored on 100 tasks, not 101.
- Released expected values and MCQ keys are kept even where they disagree with the prompt or with what Python does, because the paper graded with them.
