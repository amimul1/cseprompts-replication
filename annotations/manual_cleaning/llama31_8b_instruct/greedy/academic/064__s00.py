# ================= CSEPrompts manual cleaning =================
# task: academic/064 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called sum_evens. sum_evens should take
#   #two parameters: a minimum and a maximum. It should add up
#   #all the even numbers between minimum and maximum and
#   #return the sum.
#   #
#   #sum_evens should work inclusively: both the minimum and
#   #the maximum should be added if they are even. For example,
#   #sum_evens(2, 6) -> 12 (2 + 4 + 6 = 12)
# ---- model response below: edit from here ----
def sum_evens(min_num, max_num):
    """
    This function calculates the sum of all even numbers between min_num and max_num (inclusive).

    Args:
        min_num (int): The minimum number in the range (inclusive).
        max_num (int): The maximum number in the range (inclusive).

    Returns:
        int: The sum of all even numbers in the range.
    """
    # Initialize the sum to 0
    total_sum = 0
    
    # Loop through all numbers in the range from min_num to max_num (inclusive)
    for num in range(min_num, max_num + 1):
        # Check if the current number is even
        if num % 2 == 0:
            # If the number is even, add it to the total sum
            total_sum += num
    
    # Return the total sum
    return total_sum

# Example usage:
print(sum_evens(2, 6))  # Output: 12