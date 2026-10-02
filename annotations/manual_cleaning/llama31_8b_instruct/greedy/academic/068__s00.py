# ================= CSEPrompts manual cleaning =================
# task: academic/068 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called count_characters. count_characters
#   #should take as input a single string, and return a
#   #dictionary. In the dictionary, the keys should be
#   #characters, and the values should be the number of times
#   #each character appeared in the string.
#   #
#   #For example:
#   #
#   #  count_characters("aabbccc") -> {'a': 2, 'b': 2, 'c': 3}
#   #  count_characters("AaBbbb") -> {'A': 1, 'B': 1, 'a': 1, 'b': 3}
#   #
#   #You should not need to make any assumptions about the
#   #characters in the string: spaces, punctuation, line breaks,
#   #and any other characters should be handled automatically.
#   #You may count upper and lower case separately.
# ---- model response below: edit from here ----
def count_characters(s):
    """
    Returns a dictionary where the keys are characters from the input string
    and the values are the number of times each character appears.

    :param s: The input string
    :return: A dictionary with character counts
    """
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count