# ================= CSEPrompts manual cleaning =================
# task: codingsites/033 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the
#   absolute value of a number.
# ---- model response below: edit from here ----
def near_hundred(n):
    """
    Returns True if the given number is within 10 of 100 or 200.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is within 10 of 100 or 200, False otherwise.
    """
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)