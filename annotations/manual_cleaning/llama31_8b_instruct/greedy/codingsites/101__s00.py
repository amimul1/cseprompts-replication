# ================= CSEPrompts manual cleaning =================
# task: codingsites/101 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function that takes an array of strings and returns the words that are exactly four
#   letters.
# ---- model response below: edit from here ----
def filter_four_letter_words(word_list):
    """
    Returns a list of words from the input list that are exactly four letters long.

    Args:
        word_list (list): A list of strings.

    Returns:
        list: A list of four-letter words.
    """
    return [word for word in word_list if len(word) == 4]