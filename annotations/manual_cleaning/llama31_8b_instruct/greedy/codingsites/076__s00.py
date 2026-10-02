# ================= CSEPrompts manual cleaning =================
# task: codingsites/076 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a lambda function that takes two numbers and returns their sum.
# ---- model response below: edit from here ----
# Define a lambda function to calculate the sum of two numbers
sum_numbers = lambda x, y: x + y