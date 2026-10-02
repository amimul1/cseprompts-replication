# ================= CSEPrompts manual cleaning =================
# task: codingsites/069 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given a string, return a string where for every char in the original, there are two chars.
# ---- model response below: edit from here ----
def duplicate_chars(s):
    """
    Returns a new string where each character in the original string is duplicated.

    Args:
        s (str): The input string.

    Returns:
        str: A new string with each character duplicated.
    """
    return ''.join([c * 2 for c in s])