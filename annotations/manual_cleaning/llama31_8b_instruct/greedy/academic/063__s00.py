# ================= CSEPrompts manual cleaning =================
# task: academic/063 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called get_capitals. get_capitals should
#   #accept one parameter, a string. It should return a string
#   #containing only the capital letters from the original
#   #string: no lower-case letters, numbers, punctuation marks,
#   #or spaces.
#   #
#   #Remember, capital letters have ordinal numbers between 65
#   #("A") and 90 ("Z"). You may use the ord() function to get
#   #a letter's ordinal number.
#   #
#   #Your function should be able to handle strings with no
#   #capitals (return an empty string) and strings with all
#   #capitals (return the original string). You may assume
#   #we'll only use regular characters (no emojis, formatting
#   #characters, etc.).
# ---- model response below: edit from here ----
def get_capitals(s):
    """
    Returns a string containing only the capital letters from the original string.

    Parameters:
    s (str): The input string.

    Returns:
    str: A string containing only the capital letters from the original string.
    """
    return ''.join([c for c in s if ord(c) >= 65 and ord(c) <= 90])