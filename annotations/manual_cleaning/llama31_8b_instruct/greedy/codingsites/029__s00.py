# ================= CSEPrompts manual cleaning =================
# task: codingsites/029 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given two int values, return their sum. Unless the two values are the same, then return double
#   their sum.
# ---- model response below: edit from here ----
def double_sum(a, b):
    """
    Returns the sum of two integers. If the integers are the same, returns double their sum.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum or double sum of the input integers.
    """
    if a == b:
        return a + b + a + b
    else:
        return a + b