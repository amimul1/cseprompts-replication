# ================= CSEPrompts manual cleaning =================
# task: codingsites/114 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
#   The string length will be at least 2.
# ---- model response below: edit from here ----
def rotate_left_2(s):
    """
    Rotate a string left by 2 characters.

    Args:
        s (str): The input string.

    Returns:
        str: The rotated string with the first 2 characters moved to the end.
    """
    return s[2:] + s[:2]