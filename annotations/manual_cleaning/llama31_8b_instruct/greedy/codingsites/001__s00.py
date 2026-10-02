# ================= CSEPrompts manual cleaning =================
# task: codingsites/001 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function named capital_indexes. The function takes a single parameter, which is a
#   string. Your function should return a list of all the indexes in the string that have capital
#   letters.
# ---- model response below: edit from here ----
def capital_indexes(s):
    """
    Returns a list of indexes of capital letters in the given string.

    Args:
        s (str): The input string.

    Returns:
        list: A list of indexes of capital letters.
    """
    return [i for i, c in enumerate(s) if c.isupper()]