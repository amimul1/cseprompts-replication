# ================= CSEPrompts manual cleaning =================
# task: codingsites/105 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create a function that finds the index of a given item.
# ---- model response below: edit from here ----
def find_index(lst, item):
    """
    Returns the index of the given item in the list.

    Args:
        lst (list): The list to search in.
        item: The item to search for.

    Returns:
        int: The index of the item if found, -1 otherwise.

    Raises:
        ValueError: If the item is not found in the list.
    """
    try:
        return lst.index(item)
    except ValueError:
        return -1