# ================= CSEPrompts manual cleaning =================
# task: codingsites/028 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is
#   smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return
#   True if we are in trouble.
# ---- model response below: edit from here ----
def are_we_in_trouble(a_smile, b_smile):
    """
    Returns True if we are in trouble, False otherwise.

    We are in trouble if both monkeys are smiling or if neither of them is smiling.

    Args:
        a_smile (bool): Whether monkey a is smiling.
        b_smile (bool): Whether monkey b is smiling.

    Returns:
        bool: Whether we are in trouble.
    """
    return a_smile and b_smile or not a_smile and not b_smile