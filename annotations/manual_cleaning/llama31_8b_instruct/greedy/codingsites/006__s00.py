# ================= CSEPrompts manual cleaning =================
# task: codingsites/006 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function named add_dots that takes a string and adds "." in between each letter. For
#   example, calling add_dots("test") should return the string "t.e.s.t". Then, below the add_dots
#   function, write another function named remove_dots that removes all dots from a string.
# ---- model response below: edit from here ----
def add_dots(s):
    """
    Adds a dot between each letter in a string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with a dot between each letter.
    """
    return '.'.join(s)


def remove_dots(s):
    """
    Removes all dots from a string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with all dots removed.
    """
    return s.replace('.', '')