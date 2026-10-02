# ================= CSEPrompts manual cleaning =================
# task: codingsites/038 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Fix the last line so that it outputs the sum of 1 and 2
# ---- model response below: edit from here ----
## Sum of 1 and 2
# Define a function to calculate the sum
def calculate_sum():
    """
    This function calculates the sum of 1 and 2.
    
    Returns:
        int: The sum of 1 and 2.
    """
    # Define the numbers to be added
    num1 = 1
    num2 = 2
    
    # Calculate the sum
    total = num1 + num2
    
    # Return the sum
    return total

# Call the function and print the result
result = calculate_sum()
print("The sum of 1 and 2 is:", result)