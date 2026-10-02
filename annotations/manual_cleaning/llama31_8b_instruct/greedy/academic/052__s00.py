# ================= CSEPrompts manual cleaning =================
# task: academic/052 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called remainder. remainder should take
#   #two parameters: a dividend and a divisor. It should return
#   #the remainder when you divide the dividend by the divisor.
#   #
#   #For example:
#   # remainder(9, 3) -> 0
#   # remainder(8, 3) -> 2
#   # remainder(7, 3) -> 1
#   # remainder(6, 3) -> 0
#   #
#   #You may not use Python's built-in modulus operator. The
#   #symbol for that operator should not appear anywhere in your
#   #code.
#   #
#   #You may assume both dividend and divisor will be greater
#   #than 0
# ---- model response below: edit from here ----
## Remainder Function
### A function to calculate the remainder of a division operation without using the modulus operator.
def remainder(dividend, divisor):
    """
    Calculate the remainder of a division operation.

    Args:
        dividend (int): The number being divided.
        divisor (int): The number by which we are dividing.

    Returns:
        int: The remainder of the division operation.

    Raises:
        ZeroDivisionError: If the divisor is zero.
    """
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    return dividend