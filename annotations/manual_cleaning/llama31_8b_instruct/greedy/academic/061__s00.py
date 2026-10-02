# ================= CSEPrompts manual cleaning =================
# task: academic/061 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   input_string = "1234"
#   
#   #You may modify the lines of code above, but don't move them!
#   #When you Submit your code, we'll change these lines to
#   #assign different values to the variables.
#   
#   #Imagine that you're writing some software for a check-out
#   #register. The software tries to guess what information was
#   #entered based on its structure:
#   #
#   # - If the information entered as all numbers, then it's a
#   #   PIN number.
#   # - If the information entered was a number with a decimal,
#   #   it's a transaction amount.
#   # - If the information entered was neither, it's a password.
#   #
#   #Write some code to figure out which of these types of
#   #information the inputted string is. Print "PIN" for PIN
#   #number, "amount" for transaction amount, or "password" for
#   #password. You may assume these are the only three possible
#   #outcomes.
#   #
#   #Hint: You can do this however you want, but error handling
#   #will be easier than using conditionals.
# ---- model response below: edit from here ----
def determine_info_type(input_string):
    """
    Determine the type of information entered based on its structure.

    Args:
        input_string (str): The input string to be evaluated.

    Returns:
        str: The type of information entered ("PIN", "amount", or "password").
    """
    try:
        # Attempt to convert the input string to a float
        float(input_string)
        # If successful, it's a transaction amount
        return "amount"
    except ValueError:
        # If not a number, check if it's a PIN number
        if input_string.isdigit():
            return "PIN"
        else:
            # If not a PIN number, it's a password
            return "password"

input_string = "1234"
print(determine_info_type(input_string))