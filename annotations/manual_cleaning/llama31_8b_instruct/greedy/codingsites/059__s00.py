# ================= CSEPrompts manual cleaning =================
# task: codingsites/059 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create a function that finds how many steps it takes from a number to reach 1 by following
#   Collatz Conjecture rules.
# ---- model response below: edit from here ----
def collatz_steps(n):
    """
    Calculate the number of steps it takes to reach 1 by following the Collatz Conjecture rules.

    Args:
        n (int): The starting number.

    Returns:
        int: The number of steps it takes to reach 1.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1

    return steps