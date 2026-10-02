# ================= CSEPrompts manual cleaning =================
# task: codingsites/107 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word
#   is in the middle of the out string, e.g. "<<word>>".
# ---- model response below: edit from here ----
def make_out_string(out, word):
    """
    Returns a new string where the word is in the middle of the out string.

    Args:
        out (str): The outer string with two '<' and two '>'.
        word (str): The word to be placed in the middle of the out string.

    Returns:
        str: A new string with the word in the middle of the out string.
    """
    return out.replace('<<>>', word)
