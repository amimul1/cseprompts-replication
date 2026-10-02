# ================= CSEPrompts manual cleaning =================
# task: codingsites/078 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a regular expression that matches a string containing the word 'Python'.
# ---- model response below: edit from here ----
import re

# Define the regular expression pattern
pattern = r'\bPython\b'

# Test the pattern
string = "I love programming in Python"
match = re.search(pattern, string)

if match:
    print("The string contains the word 'Python'.")
else:
    print("The string does not contain the word 'Python'.")
