# ================= CSEPrompts manual cleaning =================
# task: academic/096 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #A palindrome is a sequence of letters that is the same
#   #forward and backward. For example, "racecar" is a
#   #palindrome.
#   #
#   #Write a function called create_palindrome. The function should
#   #have one parameter, a string. The function should return the
#   #string as a palindrome.
#   #
#   #If the string was not already a palindrome, the function should
#   #return a new string made from the original string and the
#   #reverse of the original string. For example:
#   #
#   # create_palindrome("abc") -> "abccba"
#   #
#   #However, if the string _is_ already a palindrome, the function
#   #should just return the original string by itself. For example:
#   #
#   # create_palindrome("racecar") -> "racecar"
#   #
#   #In determining whether a string is a palindrome or not, you
#   #should ignore punctuation, capitalization and spaces. For
#   #example:
#   #
#   # create_palindrome("Madam in Eden, I'm Adam") -> "Madam in Eden, I'm Adam"
#   #
#   #In creating a palindrome, though, you should use the original
#   #formatting:
#   #
#   # create_palindrome("Hello there!") -> "Hello there!!ereht olleH"
#   #
#   #You may assume that the only characters in the string will
#   #be letters, spaces, apostrophes, commas, periods, and
#   #question marks.
#   #
#   #Hint: Before checking if the string is a palindrome, get
#   #rid of the spaces and punctuation marks using the replace()
#   #method and convert the entire string to upper or lower
#   #case using the upper() or lower() methods. Remember, though,
#   #to keep the original string as your result should preserve
#   #the original punctuation and capitalization.
#   #
#   #Hint 2: There are multiple ways to do this! If you're stuck
#   #on one way, try a different one. You could use string
#   #slicing, a for loop, or some string methods. Or, try
#   #printing the string at different stages to see what's going
#   #wrong!
# ---- model response below: edit from here ----
def create_palindrome(s):
    """
    Creates a palindrome from a given string. If the string is already a palindrome, 
    it returns the original string. Otherwise, it returns the string concatenated with 
    its reverse, preserving the original formatting.

    Args:
        s (str): The input string.

    Returns:
        str: The palindrome string.
    """

    # Remove spaces and punctuation, and convert to lower case
    s = ''.join(e for e in s if e.isalnum() or e in [' ', '.', ',', '?', "'"]).lower()

    # Check if the string is a palindrome
    if s == s[::-1]:
        # If it's a palindrome, return the original string
        return s
    else:
        # If it's not a palindrome, return the string concatenated with its reverse
        return s + s[::-1]