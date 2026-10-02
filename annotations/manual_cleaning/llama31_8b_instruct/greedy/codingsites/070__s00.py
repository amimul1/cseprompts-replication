# ================= CSEPrompts manual cleaning =================
# task: codingsites/070 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Return the number of times that the string "hi" appears anywhere in the given string.
# ---- model response below: edit from here ----
def count_hi(s):
    """
    Returns the number of times the substring "hi" appears in the given string.

    Args:
        s (str): The input string to search in.

    Returns:
        int: The number of occurrences of "hi" in the string.
    """
    return s.count("hi")