# ================= CSEPrompts manual cleaning =================
# task: academic/092 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called inverted_sort. inverted_ should
#   #take as input a list of integers, and return as output a
#   #list with the integers sorted from HIGHEST to LOWEST.
#   #
#   #You may use any sorting algorithm you want: bubble, merge,
#   #insertion, selection, a new sort that you learned on your
#   #own, or even one you created yourself. You may use loops,
#   #or you may use recursion.
#   #
#   #You may not use Python's native list sort or reverse
#   #methods; you must write your own sort.
# ---- model response below: edit from here ----
def inverted_sort(lst):
    """
    Sorts a list of integers in descending order using the Bubble Sort algorithm.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A new list with the integers sorted in descending order.
    """
    # Create a copy of the input list to avoid modifying the original list
    sorted_lst = lst.copy()

    # Get the length of the list
    n = len(sorted_lst)

    # Iterate over the list n-1 times
    for i in range(n - 1):
        # Initialize a flag to track if any swaps were made in the current iteration
        swapped = False

        # Iterate over the list from the first element to the (n-i-1)th element
        for j in range(n - i - 1):
            # If the current element is smaller than the next element, swap them
            if sorted_lst[j] < sorted_lst[j + 1]:
                # Swap the elements
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
                # Set the flag to True to indicate that a swap was made
                swapped = True

        # If no swaps were made in the current iteration, the list is already sorted
        if not swapped:
            break

    # Return the sorted list
    return sorted_lst