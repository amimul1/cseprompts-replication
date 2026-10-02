# ================= CSEPrompts manual cleaning =================
# task: codingsites/111 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given a string, return a version without the first and last char, so "Hello" yields "ell". The
#   string length will be at least 2.
# ---- model response below: edit from here ----
def remove_first_last(s):
    """
    Returns a version of the input string without the first and last characters.

    Args:
        s (str): The input string.

    Returns:
        str: The input string with the first and last characters removed.
    """
    return s[1:-1]