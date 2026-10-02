# ================= CSEPrompts manual cleaning =================
# task: codingsites/072 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Return the number of times that the string "code" appears anywhere in the given string, except
#   we'll accept any letter for the 'd', so "cope" and "cooe" count.
# ---- model response below: edit from here ----
import re

def count_code_variations(s):
    """
    Count the number of occurrences of "code" with any character replacing the 'd' in the given string.

    Args:
        s (str): The input string to search in.

    Returns:
        int: The number of occurrences of "code" variations.
    """
    return len(re.findall(r'co[eou].e', s))