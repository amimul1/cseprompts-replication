# ================= CSEPrompts manual cleaning =================
# task: codingsites/035 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given a string, return a new string where "not " has been added to the front. However, if the
#   string already begins with "not", return the string unchanged.
# ---- model response below: edit from here ----
def add_not(s):
    """
    Adds "not " to the front of a string if it doesn't already start with "not".

    Args:
        s (str): The input string.

    Returns:
        str: The modified string with "not " added to the front if necessary.
    """
    if s.startswith("not "):
        return s
    else:
        return "not " + s