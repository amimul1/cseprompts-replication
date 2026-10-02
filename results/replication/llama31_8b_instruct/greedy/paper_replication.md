# Replication of CSEPrompts 2.0: llama31_8b_instruct (greedy)

Setup as in the paper: released data **as is** (no corrections), paper prompt (system + task + instruction), one zero-shot attempt (greedy), code cleaned by hand, graded by the released test cases with the paper's 0–4 rubric (Guidelines.csv), MCQs graded against the released keys.

- Model: `meta-llama/Llama-3.1-8B-Instruct` @ `0e9e39f249a16976918f6564b8830bc894c89659`; paper row: LLaMA3
- Coding results from the **manual** cleaning track; 95% bootstrap CIs over tasks.

- MCQ choices: 0/100 rows checked by hand; the others were read by the rule-based reader v2.0 (rules in docs/MANUAL_CLEANING.md).

## pass@1 (%)

| | ours [95% CI] | paper (±2, read off Fig. 3/4) | paper inside our CI? |
|---|---|---|---|
| CodingSites (n=118) | 43.2 [34.7, 51.7] | 40 | yes |
| Academic (n=100) | 37.0 [28.0, 46.0] | 30 | yes |
| MCQ accuracy (n=100) | 60.0 [50.0, 69.0] | 52 | yes |

## Label distribution (% of tasks), in the format of the release's `Results/Comparison.csv`

| Platform | No Code Written | Code not executed | All test case failed | Partial Test cases passed | All test cases passed |
|---|---|---|---|---|---|
| CodingSites | 0.00 | 11.02 | 18.64 | 27.12 | 43.22 |
| Academic | 0.00 | 9.00 | 25.00 | 29.00 | 37.00 |

## MCQ labels (% of responses; paper rubric)

| Incorrect (0) | Partially correct (1) | Correct (2) |
|---|---|---|
| 26.0 | 14.0 | 60.0 |

## Manual vs automatic cleaning

Same label on 212/218 tasks (97.2%). Automatic-track pass@1: CodingSites 43.2, Academic 37.0.

Tasks whose label differs: academic/026, codingsites/012, codingsites/015, codingsites/037, codingsites/052, codingsites/085.

## Caveats

- The release has prose test cases, not the paper's pytest files. We converted each to an executable test without changing any expected value (`data/processed/pytest/original/`); this is the closest available reconstruction of the paper's grading.
- The paper's numbers are read off its bar charts (±2 points).
- Academic/090 has no released tests (its test field holds a test-writing instruction), so Academic is scored on 100 tasks, not 101.
- Released expected values and MCQ keys are kept even where they disagree with the prompt or with what Python does, because the paper graded with them.
