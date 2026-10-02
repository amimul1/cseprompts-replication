# ================= CSEPrompts manual cleaning =================
# task: academic/071 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called check_formula. The check_formula
#   #function should take as input one parameter, a string. It
#   #should return True if the string holds a correctly
#   #formatted arithmetic integer formula according to the rules
#   #below, or False if it does not.
#   #
#   #For this problem, here are the rules that define a
#   #correctly-formatted arithmetic string:
#   #
#   # - The only characters in the string should be digits or
#   #   the five arithmetic operators: +, -, *, /, and =. Any
#   #   other characters, including spaces, periods, commas,
#   #   or any letters, are not permitted.
#   # - There may not be any consecutive arithmetic operators.
#   #   Any arithmetic operator must have a number on either
#   #   side of it.
#   # - There must be an equals sign in the formula.
#   #
#   #You do not need to worry about negative numbers or
#   #parentheses, and you do not need to worry about whether
#   #the equation is accurate. You may also assume all the
#   #numbers in the string will be only one digit.
#   #
#   #Here are some examples of valid and invalid arithmetic
#   #formulas:
#   #
#   #   Valid     Invalid
#   #   5*3=5+2   5*3+5+2 (no equals)
#   #   5=7       5= (equals sign isn't in the middle)
#   #   5=2-5     50=-5 (consecutive arithmetic operators)
#   #   6/2=5/2   a=51 (illegal character)
#   #             -5=5+2 (starts with an operator)
#   #
#   #Hint: Remember, as soon as you find *one* thing wrong
#   #with the string, you know it's invalid and can return
#   #False. So, go character-by-character through the string
#   #checking everything that could be wrong. If you don't
#   #find anything wrong, return True!
# ---- model response below: edit from here ----
def check_formula(formula):
    """
    Checks if a given string is a correctly formatted arithmetic integer formula.

    Args:
        formula (str): The formula to check.

    Returns:
        bool: True if the formula is correctly formatted, False otherwise.
    """

    # Initialize a flag to track if we've seen a number
    seen_number = False

    # Initialize a flag to track if we've seen an equals sign
    seen_equals = False

    # Iterate over each character in the formula
    for i, char in enumerate(formula):
        # If the character is a digit, set the seen_number flag to True
        if char.isdigit():
            seen_number = True
        # If the character is an operator
        elif char in '+-*/=':
            # If we've already seen an equals sign, return False
            if seen_equals:
                return False
            # If we haven't seen a number before this operator, return False
            if not seen_number:
                return False
            # If this is the first character and it's an operator, return False
            if i == 0:
                return False
            # If the previous character is also an operator, return False
            if formula[i-1] in '+-*/=':
                return False
            # Set the seen_number flag to False
            seen_number = False
        # If the character is not a digit or an operator, return False
        else:
            return False
        # If the character is an equals sign, set the seen_equals flag to True
        if char == '=':
            seen_equals = True

    # If we've reached the end of the formula and haven't seen an equals sign, return False
    if not seen_equals:
        return False

    # If we've reached the end of the formula and haven't returned False, return True
    return True