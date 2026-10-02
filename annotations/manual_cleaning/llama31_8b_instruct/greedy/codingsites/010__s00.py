# ================= CSEPrompts manual cleaning =================
# task: codingsites/010 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   A palindrome is a word that is the same forwards as backwards. If the word is the same backwards
#   as forwards, you should return True. Otherwise, you should return False.
# ---- model response below: edit from here ----
def is_palindrome(word: str) -> bool:
    """
    Checks if a word is the same forwards as backwards.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]