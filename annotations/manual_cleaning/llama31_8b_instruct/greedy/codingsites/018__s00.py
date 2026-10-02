# ================= CSEPrompts manual cleaning =================
# task: codingsites/018 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Take a list of integers (positive or negative or both) and return the sum of the absolute value
#   of each element.
# ---- model response below: edit from here ----
def sum_of_abs_values(numbers):
    """
    Calculate the sum of the absolute values of each element in a list of integers.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of the absolute values of each element in the list.
    """
    return sum(abs(num) for num in numbers)
