# ================= CSEPrompts manual cleaning =================
# task: codingsites/030 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given an int n, return the absolute difference between n and 21, except return double the
#   absolute difference if n is over 21.
# ---- model response below: edit from here ----
def diff21(n):
    """
    Returns the absolute difference between n and 21, 
    except returns double the absolute difference if n is over 21.

    Args:
        n (int): The input number.

    Returns:
        int: The absolute difference or double the absolute difference.
    """
    if n > 21:
        return (n - 21) * 2
    else:
        return abs(n - 21)