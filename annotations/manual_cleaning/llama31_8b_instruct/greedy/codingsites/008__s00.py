# ================= CSEPrompts manual cleaning =================
# task: codingsites/008 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function called longest_word that takes one argument, a list of words, and returns the
#   length of the longest word in the list.
# ---- model response below: edit from here ----
def longest_word(words):
    """
    Returns the length of the longest word in the given list.

    Args:
        words (list): A list of words.

    Returns:
        int: The length of the longest word.

    Raises:
        ValueError: If the input list is empty.
    """
    if not words:
        raise ValueError("Input list is empty")

    return max(len(word) for word in words)