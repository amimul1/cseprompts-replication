# ================= CSEPrompts manual cleaning =================
# task: academic/088 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called is_palindrome. The function should
#   #have one parameter, a string. The function should return
#   #True if the string is a palindrome, False if not.
#   #
#   #A palindrome is a sequence of letters that is the same
#   #forward and backward. For example, "racecar" is a
#   #palindrome. In determining whether a string is a palindrome
#   #or not, you should ignore punctuation, capitalization and
#   #spaces. For example, "Madam in Eden, I'm Adam" is a
#   #palindrome.
#   #
#   #You may assume that the only characters in the string will
#   #be letters, spaces, apostrophes, commas, periods, and
#   #question marks.
#   #
#   #Hint: Before checking if the string is a palindrome, get
#   #rid of the spaces and punctuation marks using the replace()
#   #method and convert the entire string to upper or lower
#   #case using the upper() or lower() methods.
#   #
#   #Hint 2: There are multiple ways to do this! If you're stuck
#   #on one way, try a different one. You could use string
#   #slicing, a for loop, or some string methods. Or, try
#   #printing the string at different stages to see what's going
#   #wrong!
# ---- model response below: edit from here ----
def is_palindrome(s):
    """
    Checks if a given string is a palindrome, ignoring spaces, punctuation, and capitalization.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """

    # Remove spaces and punctuation, and convert to lower case
    s = ''.join(e for e in s if e.isalnum()).lower()

    # Compare the string with its reverse
    return s == s[::-1]
