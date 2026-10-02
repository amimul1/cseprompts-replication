# ================= CSEPrompts manual cleaning =================
# task: academic/067 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called password_check. password_check should
#   #take as input a single string. It should return a boolean:
#   #True if the password is a valid password according to the rules
#   #below, False if it is not.
#   #
#   #A string is a valid password if it meets ALL the following
#   #conditions:
#   #
#   # - It must be at least 8 characters long.
#   # - It must contain at least one character from each of the
#   #   following categories: capital letters, lower-case letters,
#   #   numbers, and punctuation. For punctuation, the following
#   #   punctuation marks are acceptable: !@#$%&()-_[]{};':",./<>?
#   # - It may not contain any characters that do not fit into the
#   #   four categories above. This includes any punctuation marks
#   #   not listed in the bullet point above, spaces, and any other
#   #   character.
# ---- model response below: edit from here ----
import string

def password_check(password):
    """
    Checks if a given password is valid according to the rules:
    - It must be at least 8 characters long.
    - It must contain at least one character from each of the following categories: 
      capital letters, lower-case letters, numbers, and punctuation.
    - It may not contain any characters that do not fit into the four categories above.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password is valid, False otherwise.
    """

    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Define the allowed punctuation marks
    allowed_punctuation = set(string.punctuation)

    # Check if the password contains at least one character from each category
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_punctuation = any(char in allowed_punctuation for char in password)

    # If the password does not contain at least one character from each category, it's invalid
    if not (has_uppercase and has_lowercase and has_number and has_punctuation):
        return False

    # Check if the password contains any characters that do not fit into the four categories
    for char in password:
        if not (char.isalpha() or char.isdigit() or char in allowed_punctuation):
            return False

    # If the password passes all checks, it's valid
    return True
