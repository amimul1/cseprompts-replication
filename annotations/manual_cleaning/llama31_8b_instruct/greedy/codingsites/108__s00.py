# ================= CSEPrompts manual cleaning =================
# task: codingsites/108 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
#   The string length will be at least 2.
# ---- model response below: edit from here ----
### Problem Solution: Triple Last Two Characters

def triple_last_two(s):
    """
    Returns a new string made of 3 copies of the last 2 chars of the original string.

    Args:
        s (str): The input string.

    Returns:
        str: A new string made of 3 copies of the last 2 chars of the original string.
    """
    return (s[-2:] * 3)