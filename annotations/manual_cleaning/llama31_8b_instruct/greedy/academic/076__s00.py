# ================= CSEPrompts manual cleaning =================
# task: academic/076 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called digit_count. digit_count should
#   #take as input a number, which could be either a float or an
#   #integer. It should return a dictionary whose keys are digits,
#   #and whose values are the number of times that digit appears
#   #in the number.
#   #
#   #The dictionary should NOT contain any numerals that do not
#   #occur at all in the number, and it should also note contain
#   #the decimal point character if the number is a decimal.
#   #
#   #For example:
#   #
#   #  digit_count(11223) -> {1: 2, 2: 2, 3: 1}
#   #  digit_count(3.14159) -> {3: 1, 1: 2, 4: 1, 5: 1, 9: 1}
#   #
#   #Hint: You should probably convert the number to a string to
#   #count the digits, but convert the individual digits back to
#   #integers to use as keys to the dictionary.
# ---- model response below: edit from here ----
def digit_count(n):
    """
    Returns a dictionary with the count of each digit in the given number.

    Args:
        n (int or float): The number to count digits in.

    Returns:
        dict: A dictionary with digits as keys and their counts as values.
    """
    # Convert the number to a string to easily iterate over its digits
    str_n = str(n)
    
    # Remove the decimal point if the number is a float
    if '.' in str_n:
        str_n = str_n.replace('.', '')
    
    # Initialize an empty dictionary to store the digit counts
    digit_counts = {}
    
    # Iterate over each character in the string
    for char in str_n:
        # Convert the character back to an integer and use it as a key
        digit = int(char)
        
        # If the digit is already in the dictionary, increment its count
        if digit in digit_counts:
            digit_counts[digit] += 1
        # Otherwise, add the digit to the dictionary with a count of 1
        else:
            digit_counts[digit] = 1
    
    return digit_counts