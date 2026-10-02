# ================= CSEPrompts manual cleaning =================
# task: codingsites/019 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create a function that takes a number as an argument. Add up all the numbers from 1 to the
#   number you passed to the function.
# ---- model response below: edit from here ----
def sum_numbers(n):
    """
    Calculate the sum of all numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of all numbers from 1 to n.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")
    
    return sum(range(1, n + 1))
