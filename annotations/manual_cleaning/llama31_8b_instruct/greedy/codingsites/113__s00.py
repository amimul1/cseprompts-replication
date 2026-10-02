# ================= CSEPrompts manual cleaning =================
# task: codingsites/113 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given 2 strings, return their concatenation, except omit the first char of each. The strings
#   will be at least length 1.
# ---- model response below: edit from here ----
def concat_without_first_char(str1, str2):
    """
    Concatenates two strings, omitting the first character of each.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string with the first character of each omitted.
    """
    return str1[1:] + str2[1:]