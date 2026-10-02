# ================= CSEPrompts manual cleaning =================
# task: codingsites/058 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function that takes a list of lists and flattens it into a one-dimensional list.
# ---- model response below: edit from here ----
import itertools

def flatten_list(nested_list):
    """
    Flattens a list of lists into a one-dimensional list.

    Args:
        nested_list (list): A list containing lists as elements.

    Returns:
        list: A one-dimensional list containing all elements from the input list.
    """
    return list(itertools.chain(*nested_list))