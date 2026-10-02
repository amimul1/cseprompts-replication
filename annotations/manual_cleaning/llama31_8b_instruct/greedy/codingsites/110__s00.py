# ================= CSEPrompts manual cleaning =================
# task: codingsites/110 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
# ---- model response below: edit from here ----
def first_half(s):
    """
    Returns the first half of a string of even length.

    Args:
        s (str): The input string.

    Returns:
        str: The first half of the input string.

    Raises:
        ValueError: If the input string has an odd length.
    """
    if len(s) % 2 != 0:
        raise ValueError("Input string must have an even length")
    return s[:len(s) // 2]