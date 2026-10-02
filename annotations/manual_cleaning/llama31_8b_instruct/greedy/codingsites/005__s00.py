# ================= CSEPrompts manual cleaning =================
# task: codingsites/005 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function named only_ints that takes two parameters. Your function should return True if
#   both parameters are integers, and False otherwise.
# ---- model response below: edit from here ----
def only_ints(a, b):
    """
    Returns True if both parameters are integers, False otherwise.

    Args:
        a (any): The first parameter to check.
        b (any): The second parameter to check.

    Returns:
        bool: True if both parameters are integers, False otherwise.
    """
    return isinstance(a, int) and isinstance(b, int)