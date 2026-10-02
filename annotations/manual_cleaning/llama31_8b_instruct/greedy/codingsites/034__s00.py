# ================= CSEPrompts manual cleaning =================
# task: codingsites/034 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given 2 int values, return True if one is negative and one is positive. Except if the parameter
#   "negative" is True, then return True only if both are negative.
# ---- model response below: edit from here ----
def has_diff_sign(a, b, negative=False):
    """
    Returns True if one of the numbers has a different sign than the other.
    If negative is True, returns True only if both numbers are negative.

    Args:
        a (int): The first number.
        b (int): The second number.
        negative (bool): Whether to return True only if both numbers are negative. Defaults to False.

    Returns:
        bool: Whether the numbers have different signs or both are negative.
    """
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)