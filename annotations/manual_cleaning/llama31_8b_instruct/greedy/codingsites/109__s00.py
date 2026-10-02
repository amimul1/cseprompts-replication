# ================= CSEPrompts manual cleaning =================
# task: codingsites/109 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given a string, return the string made of its first two chars, so the String "Hello" yields
#   "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and
#   the empty string "" yields the empty string "".
# ---- model response below: edit from here ----
def first_two_chars(s):
    """
    Returns the string made of the first two characters of the input string.
    If the string is shorter than 2 characters, returns the string as is.

    Args:
        s (str): The input string.

    Returns:
        str: The string made of the first two characters of the input string.
    """
    return s[:2]