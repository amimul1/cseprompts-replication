# ================= CSEPrompts manual cleaning =================
# task: academic/009 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate
#   for your car, with your choice of letters and numbers instead of random ones. Among the
#   requirements, though, are:
#   
#   “All vanity plates must start with at least two letters.”
#   “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2
#   characters.”
#   “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222
#   would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used
#   cannot be a ‘0’.”
#   “No periods, spaces, or punctuation marks are allowed.”
#   Implement a program that prompts the user for a vanity plate and then output Valid if meets all
#   of the requirements or Invalid if it does not. Assume that any letters in the user’s input will
#   be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all
#   requirements and False if it does not. Assume that s will be a str. You’re welcome to implement
#   additional functions for is_valid to call (e.g., one function per requirement).
# ---- model response below: edit from here ----
def has_at_least_two_letters(s):
    """
    Checks if the string has at least two letters.
    
    Args:
    s (str): The input string.
    
    Returns:
    bool: True if the string has at least two letters, False otherwise.
    """
    return sum(c.isalpha() for c in s) >= 2


def has_no_numbers_in_middle(s):
    """
    Checks if the string has no numbers in the middle.
    
    Args:
    s (str): The input string.
    
    Returns:
    bool: True if the string has no numbers in the middle, False otherwise.
    """
    return all(c.isalpha() or c == s[-1] for c in s[:-1])


def has_no_zero_as_first_number(s):
    """
    Checks if the first number used is not '0'.
    
    Args:
    s (str): The input string.
    
    Returns:
    bool: True if the first number used is not '0', False otherwise.
    """
    if s[-1].isdigit():
        return s[-1] != '0'
    return True


def has_no_special_chars(s):
    """
    Checks if the string contains no special characters.
    
    Args:
    s (str): The input string.
    
    Returns:
    bool: True if the string contains no special characters, False otherwise.
    """
    return s.isalnum()


def is_valid(s):
    """
    Checks if the string meets all requirements for a vanity plate.
    
    Args:
    s (str): The input string.
    
    Returns:
    bool: True if the string meets all requirements, False otherwise.
    """
    return (len(s) >= 2 and len(s) <= 6 and 
            has_at_least_two_letters(s) and 
            has_no_numbers_in_middle(s) and 
            has_no_zero_as_first_number(s) and 
            has_no_special_chars(s))


def main():
    s = input("Enter a vanity plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()