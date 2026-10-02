# ================= CSEPrompts manual cleaning =================
# task: codingsites/098 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create a function that takes a string and returns a string with its letters in alphabetical
#   order.
# ---- model response below: edit from here ----
def alphabetical_order(s):
    """
    Returns a string with its letters in alphabetical order.

    Args:
        s (str): The input string.

    Returns:
        str: The input string with its letters in alphabetical order.
    """
    return ''.join(sorted(s))