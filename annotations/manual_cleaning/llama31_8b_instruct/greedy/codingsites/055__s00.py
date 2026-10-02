# ================= CSEPrompts manual cleaning =================
# task: codingsites/055 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function named add_dots that takes a string and adds "." in between each letter. Write
#   another function named remove_dots that removes all dots.
# ---- model response below: edit from here ----
def add_dots(input_string):
    """
    Adds a dot between each letter in the input string.

    Args:
        input_string (str): The input string to add dots to.

    Returns:
        str: A new string with a dot between each letter.
    """
    return '.'.join(input_string)


def remove_dots(input_string):
    """
    Removes all dots from the input string.

    Args:
        input_string (str): The input string to remove dots from.

    Returns:
        str: A new string with all dots removed.
    """
    return input_string.replace('.', '')
