# ================= CSEPrompts manual cleaning =================
# task: codingsites/040 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Loop through and print out all even numbers from the numbers list in the same order they are
#   received. Don't print any numbers that come after 237 in the sequence
# ---- model response below: edit from here ----

# Define a list of numbers
numbers = [12, 45, 7, 23, 56, 89, 34, 19, 237, 98, 100, 102, 104]

# Loop through the list and print even numbers before 237
for num in numbers:
    if num < 237 and num % 2 == 0:
        print(num)