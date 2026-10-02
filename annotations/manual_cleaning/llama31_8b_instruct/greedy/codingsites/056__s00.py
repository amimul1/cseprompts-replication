# ================= CSEPrompts manual cleaning =================
# task: codingsites/056 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your
#   code should find the biggest number of consecutive zeros in the string.
# ---- model response below: edit from here ----
def find_longest_zeros(binary_string):
    """
    Finds the longest sequence of consecutive zeros in a binary string.

    Args:
        binary_string (str): A string consisting of only zeros and ones.

    Returns:
        int: The length of the longest sequence of consecutive zeros.
    """
    if not binary_string:
        return 0

    max_zeros = 0
    current_zeros = 0

    for char in binary_string:
        if char == '0':
            current_zeros += 1
            max_zeros = max(max_zeros, current_zeros)
        else:
            current_zeros = 0

    return max_zeros