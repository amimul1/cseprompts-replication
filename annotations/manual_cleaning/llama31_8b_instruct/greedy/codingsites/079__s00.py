# ================= CSEPrompts manual cleaning =================
# task: codingsites/079 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function that takes two sets and returns their union, intersection, and difference.
# ---- model response below: edit from here ----
def set_operations(set1, set2):
    """
    This function performs set operations on two input sets.

    Args:
        set1 (set): The first set.
        set2 (set): The second set.

    Returns:
        tuple: A tuple containing the union, intersection, and difference of the two sets.
    """
    # Calculate the union of the two sets
    union = set1.union(set2)
    
    # Calculate the intersection of the two sets
    intersection = set1.intersection(set2)
    
    # Calculate the difference of the two sets
    difference = set1.difference(set2) if len(set1) >= len(set2) else set2.difference(set1)
    
    return union, intersection, difference