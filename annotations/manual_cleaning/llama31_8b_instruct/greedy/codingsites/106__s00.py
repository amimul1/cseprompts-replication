# ================= CSEPrompts manual cleaning =================
# task: codingsites/106 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create a function that takes a word and returns true if the word has two consecutive identical
#   letters.
# ---- model response below: edit from here ----
def has_consecutive_identical_letters(word):
    """
    Returns True if the word has two consecutive identical letters, False otherwise.

    Args:
        word (str): The input word to check.

    Returns:
        bool: Whether the word has two consecutive identical letters.
    """
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False