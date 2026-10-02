# ================= CSEPrompts manual cleaning =================
# task: codingsites/036 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given a non-empty string and an int n, return a new string where the char at index n has been
#   removed. The value of n will be a valid index of a char in the original string (i.e. n will be
#   in the range 0..len(str)-1 inclusive).
# ---- model response below: edit from here ----
def remove_char_at_index(s, n):
    """
    Returns a new string where the char at index n has been removed.

    Args:
        s (str): The input string.
        n (int): The index of the character to be removed.

    Returns:
        str: A new string with the character at index n removed.
    """
    return s[:n] + s[n+1:]