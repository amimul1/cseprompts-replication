# ================= CSEPrompts manual cleaning =================
# task: academic/053 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called sortString. sortString should take
#   #one parameter as input, a string. If the input is not a
#   #string, sortString should return the string "Not a string!"
#   #If the input is a string, sortString should return a four-
#   #line string according to the following directions:
#   #
#   # - On the first line should be each capital letter in the
#   #   string, in the order in which they appear.
#   # - On the second line should be each lower-case letter in
#   #   the string, in the order in which they appear.
#   # - On the third line should be each punctuation mark or
#   #   numeral in the string, in the order in which they
#   #   appear.
#   # - On the fourth line should be an integer representing
#   #   how many spaces were found in the string.
#   #
#   #There should be no other text in the string that you output
#   #besides these four lines and the line breaks between them.
#   #To insert a line break into a string, insert the character
#   #sequence "\n". For example, line1 + "\n" + line2 would give
#   #a string with the first two lines and a line break in
#   #between. You may assume that the string will only be
#   #letters, spaces, and punctuation -- no numbers, line breaks,
#   #tabs, etc.
#   #
#   #For example, calling sortString("Hello, world!!1" should
#   #return: "H\nelloworld\n,!!1\n1", which would look like this
#   #when printed:
#   #H
#   #elloworld
#   #,!!1
#   #1
#   #
#   #Hint: Use the ord() function! Remember, when you pass a
#   #one-character string into ord(), it returns a number.
#   #
#   # - Lower-case letters will return a number from 97 to 122.
#   # - Upper-case letters will return a number from 65 to 90.
#   # - Puncutation marks and numbers will return a number from
#   #   33 to 64.
#   # - Spaces will return the number 32.
#   #
#   #So, you can check if a letter is lowercase by seeing if
#   #ord(letter) is between 97 and 122 (inclusive; 97 is 'a',
#   #122 is 'z'), and so on for uppercase and punctuation.
#   #
#   #Hint 2: Build up three separate strings (one for
#   #uppercase, one for lowercase, and one for punctuation),
#   #then combine them and the count of the number of spaces
#   #into a string to return at the end.
# ---- model response below: edit from here ----
def sortString(s):
    """
    Sorts a string into four lines: 
    - Uppercase letters, in order of appearance
    - Lowercase letters, in order of appearance
    - Punctuation and numbers, in order of appearance
    - Number of spaces found in the string

    Args:
        s (str): The input string to be sorted

    Returns:
        str: A four-line string with the sorted characters and the count of spaces
    """

    # Check if the input is a string
    if not isinstance(s, str):
        return "Not a string!"

    # Initialize empty strings to store the sorted characters
    uppercase = ""
    lowercase = ""
    punctuation = ""
    space_count = 0

    # Iterate over each character in the string
    for char in s:
        # Check the type of the character
        if char.isupper():
            # If uppercase, add it to the uppercase string
            uppercase += char
        elif char.islower():
            # If lowercase, add it to the lowercase string
            lowercase += char
        elif char.isdigit() or not char.isalnum() and not char.isspace():
            # If punctuation or a number, add it to the punctuation string
            punctuation += char
        elif char.isspace():
            # If a space, increment the space count
            space_count += 1

    # Return the sorted string
    return uppercase + "\n" + lowercase + "\n" + punctuation + "\n" + str(space_count)
