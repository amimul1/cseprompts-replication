# ================= CSEPrompts manual cleaning =================
# task: codingsites/071 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Return True if the string "cat" and "dog" appear the same number of times in the given string.
# ---- model response below: edit from here ----
def count_cat_dog(s):
    """
    Returns True if the string "cat" and "dog" appear the same number of times in the given string.

    Args:
        s (str): The input string to search for "cat" and "dog".

    Returns:
        bool: True if "cat" and "dog" appear the same number of times, False otherwise.
    """
    return s.count("cat") == s.count("dog")