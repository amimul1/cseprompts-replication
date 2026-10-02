# ================= CSEPrompts manual cleaning =================
# task: codingsites/022 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   There is a single operator in Python, capable of providing the remainder of a division
#   operation. Two numbers are passed as parameters. The first parameter divided by the second
#   parameter will have a remainder, possibly zero. Return that value.
# ---- model response below: edit from here ----
def calculate_remainder(dividend, divisor):
    """
    Calculate the remainder of the division of dividend by divisor.

    Args:
        dividend (int): The number being divided.
        divisor (int): The number by which we are dividing.

    Returns:
        int: The remainder of the division.

    Raises:
        ZeroDivisionError: If divisor is zero.
    """
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return dividend % divisor