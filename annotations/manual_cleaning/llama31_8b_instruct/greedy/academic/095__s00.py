# ================= CSEPrompts manual cleaning =================
# task: academic/095 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called count_squares. This function
#   #should take as input a list of integers, and return as
#   #output a single integer. The number the function returns
#   #should be the number of perfect squares it found in the
#   #list of integers. You may assume every number in the list
#   #is between 1 and 1 billion (1,000,000,000).
#   #
#   #For example:
#   #
#   # count_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) -> 3
#   # count_squares([1, 4, 9, 16, 25, 36, 49, 64]) -> 8
#   # count_squares([2, 3, 5, 6, 7, 8, 10, 11]) -> 0
#   #
#   #For this problem, 0 is considered a square.
#   #
#   #Hint: Don't get caught up trying to "remember" how to
#   #calculate if a number is a square: we've never done it
#   #before, but we've covered all the tools you need to do it
#   #in one of several different ways.
# ---- model response below: edit from here ----
### Counting Perfect Squares in a List of Integers
import math

def count_squares(numbers):
    """
    Counts the number of perfect squares in a list of integers.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The number of perfect squares in the list.
    """
    count = 0
    for num in numbers:
        # Check if the square root of the number is an integer
        if math.sqrt(num) == int(math.sqrt(num)):
            count += 1
    return count

# Example usage:
print(count_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: 3
print(count_squares([1, 4, 9, 16, 25, 36, 49, 64]))  # Output: 8
print(count_squares([2, 3, 5, 6, 7, 8, 10, 11]))  # Output: 