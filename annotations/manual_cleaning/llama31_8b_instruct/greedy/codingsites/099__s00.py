# ================= CSEPrompts manual cleaning =================
# task: codingsites/099 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function that takes a positive integer and return its factorial.
# ---- model response below: edit from here ----
def factorial(n):
    """
    Calculate the factorial of a positive integer.

    Args:
        n (int): A positive integer.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result