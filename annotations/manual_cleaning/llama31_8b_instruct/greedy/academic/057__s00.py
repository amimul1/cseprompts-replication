# ================= CSEPrompts manual cleaning =================
# task: academic/057 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   n = 5
#   
#   #You may modify the lines of code above, but don't move them!
#   #When you Submit your code, we'll change these lines to
#   #assign different values to the variables.
#   
#   #Write some code that will find and print the factorial of
#   #the number given by n above. You may not import anything
#   #from the Python math library.
#   #
#   #Hint: Use a while loop, but be careful to avoid an infinite
#   #loop!
# ---- model response below: edit from here ----

n = 5

def calculate_factorial(n):
    """
    Calculate the factorial of a given number n.
    
    Args:
        n (int): The number to calculate the factorial of.
    
    Returns:
        int: The factorial of n.
    """
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

print(calculate_factorial(n))