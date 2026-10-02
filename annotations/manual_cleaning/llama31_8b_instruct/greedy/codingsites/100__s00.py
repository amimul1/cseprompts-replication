# ================= CSEPrompts manual cleaning =================
# task: codingsites/100 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create a function that takes an array of numbers and returns the mean value.
# ---- model response below: edit from here ----
def calculate_mean(numbers):
    """
    Calculate the mean of an array of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The mean of the input numbers.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")

    return sum(numbers) / len(numbers)