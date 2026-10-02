# ================= CSEPrompts manual cleaning =================
# task: codingsites/093 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Two strings are anagrams if you can make one from the other by rearranging the letters. Write a
#   function named is_anagram that takes two strings as its parameters. Your function should return
#   True if the strings are anagrams, and False otherwise.
# ---- model response below: edit from here ----

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    # Remove any whitespace and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted versions of the strings are equal
    return sorted(str1) == sorted(str2)
