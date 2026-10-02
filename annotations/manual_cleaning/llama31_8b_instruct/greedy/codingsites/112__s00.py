# ================= CSEPrompts manual cleaning =================
# task: codingsites/112 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string
#   on the outside and the longer string on the inside. The strings will not be the same length, but
#   they may be empty (length 0).
# ---- model response below: edit from here ----
def make_out_string(a, b):
    """
    Returns a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside.

    Args:
        a (str): The first string.
        b (str): The second string.

    Returns:
        str: The resulting string.
    """
    if len(a) >= len(b):
        return a + b + a
    else:
        return b + a + b
