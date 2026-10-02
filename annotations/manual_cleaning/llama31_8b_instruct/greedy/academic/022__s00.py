# ================= CSEPrompts manual cleaning =================
# task: academic/022 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   implement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein
#   is_valid still expects a str as input and returns True if that str meets all requirements and
#   False if it does not, but main is only called if the value of __name__ is "__main__":
#   
#   here is the Vanity Plates from Problem Set 2:
#   
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
#   In plates.py, implement a program that prompts the user for a vanity plate and then output Valid
#   if meets all of the requirements or Invalid if it does not. Assume that any letters in the
#   user’s input will be uppercase. Structure your program per the below, wherein is_valid returns
#   True if s meets all requirements and False if it does not. Assume that s will be a str. You’re
#   welcome to implement additional functions for is_valid to call (e.g., one function per
#   requirement).
#   
#   def main():
#       plate = input("Plate: ")
#       if is_valid(plate):
#           print("Valid")
#       else:
#           print("Invalid")
#   
#   
#   def is_valid(s):
#       ...
#   
#   
#   main()
# ---- model response below: edit from here ----
def has_at_least_two_letters(s):
    """Check if the string has at least two letters."""
    return sum(c.isalpha() for c in s) >= 2


def has_no_numbers_in_middle(s):
    """Check if there are no numbers in the middle of the string."""
    return all(c.isalpha() or c.isdigit() for c in s[:-1]) or len(s) <= 2


def has_no_leading_zero(s):
    """Check if the first number in the string is not a zero."""
    if s[0].isdigit():
        return s[0] != '0'
    return True


def has_no_special_chars(s):
    """Check if the string contains no special characters."""
    return s.isalnum()


def is_valid(s):
    """Check if the vanity plate meets all requirements."""
    return (len(s) >= 2 and len(s) <= 6 and 
            has_at_least_two_letters(s) and 
            has_no_numbers_in_middle(s) and 
            has_no_leading_zero(s) and 
            has_no_special_chars(s))


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()