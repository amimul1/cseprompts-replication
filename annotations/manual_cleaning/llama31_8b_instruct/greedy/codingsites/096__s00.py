# ================= CSEPrompts manual cleaning =================
# task: codingsites/096 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Define a function named up_down that takes a single number as its parameter. Your function
#   return a tuple containing two numbers; the first should be one lower than the parameter, and the
#   second should be one higher.
# ---- model response below: edit from here ----
def up_down(n):
    """
    Returns a tuple containing two numbers: one lower and one higher than the input number.

    Args:
        n (int): The input number.

    Returns:
        tuple: A tuple containing two numbers.
    """
    return (n - 1, n + 1)