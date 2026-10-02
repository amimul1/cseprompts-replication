# ================= CSEPrompts manual cleaning =================
# task: codingsites/024 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given two numbers, return True if the sum of both numbers is less than 100. Otherwise return
#   False.
# ---- model response below: edit from here ----
def sum_less_than_100(a, b):
    """
    Returns True if the sum of two numbers is less than 100, False otherwise.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        bool: Whether the sum of the two numbers is less than 100.
    """
    return a + b < 100