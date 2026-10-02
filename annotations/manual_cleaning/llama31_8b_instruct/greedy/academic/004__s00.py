# ================= CSEPrompts manual cleaning =================
# task: academic/004 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   implement a program that prompts the user for an arithmetic expression and then calculates and
#   outputs the result as a floating-point value formatted to one decimal place. Assume that the
#   user’s input will be formatted as x y z, with one space between x and y and one space between y
#   and z, wherein:
#   
#   x is an integer
#   y is +, -, *, or /
#   z is an integer
#   For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /,
#   then z will not be 0.
# ---- model response below: edit from here ----
def calculate_expression():
    """
    Prompts the user for an arithmetic expression, calculates the result, 
    and outputs the result as a floating-point value formatted to one decimal place.
    """
    
    # Prompt the user for an arithmetic expression
    expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")
    
    # Split the input string into three parts: x, y, and z
    x, y, z = expression.split()
    
    # Convert x and z to integers
    x = int(x)
    z = int(z)
    
    # Perform the arithmetic operation based on the operator y
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        # Check if z is not zero to avoid division by zero error
        if z == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = x / z
    else:
        print("Error: Invalid operator. Only +, -, *, and / are allowed.")
        return
    
    # Format the result to one decimal place and print it
    print(f"The result is: {result:.1f}")

# Call the function to start the program
calculate_expression()