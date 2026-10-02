# ================= CSEPrompts manual cleaning =================
# task: codingsites/095 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Define a function named all_equal that takes a list and checks whether all elements in the list
#   are the same.
# ---- model response below: edit from here ----
def all_equal(lst):
    """
    Checks if all elements in the list are equal.

    Args:
        lst (list): The list to check.

    Returns:
        bool: True if all elements are equal, False otherwise.
    """
    return len(set(lst)) == 1