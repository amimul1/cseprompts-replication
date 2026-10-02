# ================= CSEPrompts manual cleaning =================
# task: codingsites/002 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function named mid that takes a string as its parameter. Your function should extract
#   and return the middle letter. If the length of the string is even, you should return the middle
#   two letters.
# ---- model response below: edit from here ----
def mid(s):
    """
    Extract and return the middle letter(s) of a given string.
    
    If the length of the string is even, return the middle two letters.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    str: The middle letter(s) of the string.
    """
    length = len(s)
    middle_index = length // 2
    
    if length % 2 == 0:
        # If the length is even, return the middle two letters
        return s[middle_index - 1:middle_index + 1]
    else:
        # If the length is odd, return the middle letter
        return s[middle_index]