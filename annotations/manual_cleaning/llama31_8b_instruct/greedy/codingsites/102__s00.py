# ================= CSEPrompts manual cleaning =================
# task: codingsites/102 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create a function that takes an array of arrays with numbers. Return a new (single) array with
#   the largest numbers of each.
# ---- model response below: edit from here ----
def largest_numbers(arrays):
    """
    Returns a new array with the largest numbers from each subarray.

    Args:
        arrays (list): A list of lists with numbers.

    Returns:
        list: A new list with the largest numbers from each subarray.
    """
    return [max(subarray) for subarray in arrays]