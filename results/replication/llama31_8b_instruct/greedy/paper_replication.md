# Replication of CSEPrompts 2.0: llama31_8b_instruct (greedy)

Setup as in the paper: released data **as is** (no corrections), paper prompt (system + task + instruction), one zero-shot attempt (greedy), code cleaned by hand, graded by the released test cases with the paper's 0–4 rubric (Guidelines.csv), MCQs graded against the released keys.

- Model: `meta-llama/Llama-3.1-8B-Instruct` @ `0e9e39f249a16976918f6564b8830bc894c89659`; paper row: LLaMA3
- Coding results from the **auto (manual not available yet)** cleaning track; 95% bootstrap CIs over tasks.

> **Not final:**
> - No manual-track evaluation yet (step 4 of docs/REPLICATION_PAPER.md).
> - No MCQ score yet (step 5).

## pass@1 (%)

| | ours [95% CI] | paper (±2, read off Fig. 3/4) | paper inside our CI? |
|---|---|---|---|
| CodingSites (n=118) | 43.2 [34.7, 52.5] | 40 | yes |
| Academic (n=100) | 37.0 [28.0, 46.0] | 30 | yes |

## Label distribution (% of tasks), in the format of the release's `Results/Comparison.csv`

| Platform | No Code Written | Code not executed | All test case failed | Partial Test cases passed | All test cases passed |
|---|---|---|---|---|---|
| CodingSites | 0.00 | 12.71 | 16.95 | 27.12 | 43.22 |
| Academic | 0.00 | 8.00 | 26.00 | 29.00 | 37.00 |

## Caveats

- The release has prose test cases, not the paper's pytest files. We converted each to an executable test without changing any expected value (`data/processed/pytest/original/`); this is the closest available reconstruction of the paper's grading.
- The paper's numbers are read off its bar charts (±2 points).
- Academic/090 has no released tests (its test field holds a test-writing instruction), so Academic is scored on 100 tasks, not 101.
- Released expected values and MCQ keys are kept even where they disagree with the prompt or with what Python does, because the paper graded with them.
