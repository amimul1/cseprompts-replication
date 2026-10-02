# ================= CSEPrompts manual cleaning =================
# task: codingsites/025 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create a function that takes a number as its only argument and returns True if it's less than or
#   equal to zero, otherwise return False.
# ---- model response below: edit from here ----
def is_less_than_or_equal_to_zero(num):
    """
    Returns True if the input number is less than or equal to zero, False otherwise.

    Args:
        num (int or float): The number to check.

    Returns:
        bool: Whether the number is less than or equal to zero.
    """
    return num <= 0