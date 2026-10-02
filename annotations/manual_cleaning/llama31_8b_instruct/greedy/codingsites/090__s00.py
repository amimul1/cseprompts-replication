# ================= CSEPrompts manual cleaning =================
# task: codingsites/090 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function named double_letters that takes a string as its parameter. The function should
#   return True if there are two identical letters in a row in the string, and False otherwise.
# ---- model response below: edit from here ----
def double_letters(s):
    """
    Returns True if there are two identical letters in a row in the string, False otherwise.

    Args:
        s (str): The input string to check.

    Returns:
        bool: Whether there are two identical letters in a row.
    """
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False