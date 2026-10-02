# ================= CSEPrompts manual cleaning =================
# task: codingsites/032 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
# ---- model response below: edit from here ----
def makes10(a, b):
    """
    Returns True if one of the numbers is 10 or their sum is 10.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        bool: Whether one of the numbers is 10 or their sum is 10.
    """
    return a == 10 or b == 10 or a + b == 10