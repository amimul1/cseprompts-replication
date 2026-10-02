# ================= CSEPrompts manual cleaning =================
# task: codingsites/026 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create a function that takes a list and returns the first element.
# ---- model response below: edit from here ----
def get_first_element(lst):
    """
    Returns the first element of a list.

    Args:
        lst (list): The input list.

    Returns:
        The first element of the list, or None if the list is empty.

    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    return lst[0] if lst else None
