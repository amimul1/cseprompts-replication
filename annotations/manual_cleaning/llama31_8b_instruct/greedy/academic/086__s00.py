# ================= CSEPrompts manual cleaning =================
# task: academic/086 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called count_positive_evens. This function
#   #should take as input a list of integers, and return as
#   #output a single integer. The number the function returns
#   #should be the count of numbers from the list that were both
#   #positive and even.
#   #
#   #For example:
#   #
#   # count_positive_evens([5, 7, 9, 8, -1, -2, -3]) -> 1
#   # count_positive_evens([2, 4, 6, 8, 10, 12, 15]) -> 6
#   # count_positive_evens([-2, -4, -6, -8, -10, 1]) -> 0
#   #
#   #0 should be not counted as a positive even number.
#   #
#   #Hint: Remember, even numbers are numbers that have a
#   #remainder of 0 when divided by 2.
# ---- model response below: edit from here ----
def count_positive_evens(numbers):
    """
    Counts the number of positive even numbers in a list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The count of positive even numbers in the list.
    """
    count = 0
    for num in numbers:
        # Check if the number is positive and even
        if num > 0 and num % 2 == 0:
            count += 1
    return count