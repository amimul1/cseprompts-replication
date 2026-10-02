# ================= CSEPrompts manual cleaning =================
# task: codingsites/073 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given two strings, return True if either of the strings appears at the very end of the other
#   string, ignoring upper/lower case differences (in other words, the computation should not be
#   "case sensitive"). Note: s.lower() returns the lowercase version of a string.
# ---- model response below: edit from here ----
def end_match(s1, s2):
    """
    Returns True if either s1 or s2 appears at the end of the other string, ignoring case differences.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.

    Returns:
        bool: True if either string appears at the end of the other, False otherwise.
    """
    return s1.lower().endswith(s2.lower()) or s2.lower().endswith(s1.lower())