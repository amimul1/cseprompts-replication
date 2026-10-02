# ================= CSEPrompts manual cleaning =================
# task: codingsites/103 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create a function that takes a string and returns the middle character(s). If the word's length
#   is odd, return the middle character. If the word's length is even, return the middle two
#   characters.
# ---- model response below: edit from here ----
def get_middle_char(s):
    """
    Returns the middle character(s) of a given string.

    If the word's length is odd, returns the middle character.
    If the word's length is even, returns the middle two characters.

    Args:
        s (str): The input string.

    Returns:
        str: The middle character(s) of the input string.
    """
    length = len(s)
    middle_index = length // 2

    if length % 2 == 0:  # Even length
        return s[middle_index - 1:middle_index + 1]
    else:  # Odd length
        return s[middle_index]
