# Manual code-cleaning guidelines

*Version 1.0, fixed 2026-09-29 before any model output was cleaned. If a rule changes, bump the version,
note the date, and re-check files cleaned under the old rule.*

The CSEPrompts 2.0 paper says the model responses "are manually cleaned to isolate the code" and then
tested. The paper gives no further rules, so these are ours. They are designed to:

- **isolate the model's code, never improve it.** Cleaning must not change whether the code passes;
- **be reproducible.** A second annotator following these rules should produce the same file;
- **match the automatic extractor** (`src/cseprompts/harness/extract.py`), so the two tracks can be compared.

## The files

`python scripts/prepare_cleaning.py --run <run dir>` creates one file per coding response:

```
annotations/manual_cleaning/<model>/<run>/<split>/NNN__sKK.py
```

Each file has a comment header (task id, task type, the prompt), then the line
`# ---- model response below: edit from here ----`, then the model's **raw** response.
Edit only below that line. Existing files are never overwritten, so your work is safe if the script
is re-run.

When you finish a file, change `# MANUAL_STATUS: TODO` in the header to:

| status | when |
|---|---|
| `DONE` | you isolated the code |
| `NO_CODE` | the response contains no Python code at all (only prose, only pseudo-code, a refusal...) |

Only DONE and NO_CODE files are scored. `scripts/evaluate.py --track manual` reports how many are
still TODO.

## Rules

1. **Delete everything that is not code:** explanations, markdown fences (```` ``` ````), headings,
   bullet points, "Output:" blocks, sample runs, and `>>>` prompts (keep the code after `>>> `).
2. **Keep the code exactly as written.** Do not fix bugs, typos, indentation, names, imports or logic.
   Do not add anything, not even a missing `import` or a call to `main()`.
3. **What counts as "the solution" depends on the task type** (shown in the header):
   - **FUNCTION / CLASS tasks:** keep the definitions the task asks for, plus the imports, helper
     functions, classes and constants they use. **Delete** example calls, `print(...)` demos, test code,
     `input()` prompts, and `if __name__ == "__main__":` blocks.
   - **PROGRAM tasks** (the prompt says "prompt the user", "read", "print"...): keep the **whole program**,
     including `input()` calls, prints, `main()` and `if __name__ == "__main__": main()`.
   - **VARIABLES tasks** (GT CS1301: variables at the top that "we'll change"): keep the whole script,
     including the variable assignments at the top.
4. **Several code blocks:**
   - If they are parts of one solution (helper + main function), keep them all, in order.
   - If they are **alternative** solutions, keep the one the model presents as its final answer (e.g.
     "Here's the corrected/improved version"); if it does not say, keep the **first complete** one.
   - A block that only demonstrates or tests the solution follows rule 3.
5. **Truncated responses** (the file ends mid-code because the length limit was hit): clean what is
   there; do not complete it.
6. **Pseudo-code or code in another language** is not Python code: if that is all there is, mark `NO_CODE`.
7. When unsure, choose the option that changes the model's behaviour the least, and add a comment line
   `# MANUAL_NOTE: <why>` right under the status line in the header.

## Quality control (for the paper)

- Clean in the random order of `annotations/manual_cleaning/<model>/<run>/manifest.csv`. If time is
  short, the first N files are a random sample.
- **Second annotator:** have a second person (e.g. Nishat or a labmate) clean a random 10–20% of the files
  independently, into a copy of the directory, and report agreement on the resulting labels. The
  evaluation already compares the manual track with the automatic one.
- Commit the annotation files after each session (`git add annotations && git commit`).

## MCQ answers (version 1.0, fixed 2026-10-02)

The paper graded MCQs against the answer keys; it does not say how a free-text response was read.
These rules decide **which option(s) a response chose**. They are applied by hand (`chosen`) or by the
rule-based reader `cseprompts.harness.mcq.read_choice` (`scripts/mcq.py autofill` → `auto_chosen`),
which was checked against a full manual reading of the Llama-3.1-8B greedy sheet (100/100 rows agree).
The model's response is never edited.

1. **The answer is what the response states as its answer**: "The correct answer is …", "The correct
   options are …", "The output of the line of code above is …", "… resolves to True", or
   "'None of the above' is correct".
2. **If it states an answer more than once, the last statement counts** (e.g. "However, the most accurate
   option is …"). A closing remark that names no option ("the correct options are the ones that …") is
   not a new answer.
3. **Reasoning that contradicts the stated answer does not change it.** Example: "The correct answer is:
   True … so `bool("")` will return False" chose **True**. Such rows are worth a manual look, but the
   stated answer is what is graded.
4. **Text is matched to the options as written**, ignoring backticks, list bullets, commas and `and`
   between assignments. Quotes count: `"2"` is the option `"2"`, not `2`. A list of several answers
   chooses all of them. "Option N" means the N-th listed option.
5. **An answer that is not one of the options is no choice** (graded 0), e.g. `cost = 5001` when no
   option has 5001. So is a response with no answer statement (e.g. one that loops until the length limit).
6. Identical options (the release repeats some) are all chosen when their text is chosen.
