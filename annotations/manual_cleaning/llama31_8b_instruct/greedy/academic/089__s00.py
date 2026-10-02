# ================= CSEPrompts manual cleaning =================
# task: academic/089 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called not_list. not_list should have two
#   #parameters: a list of booleans and a list of integers.
#   #
#   #The list of integers will represent indices for the list of
#   #booleans. not_list should switch the values of all the
#   #booleans located at those indices.
#   #
#   #For example:
#   #
#   # bool_list = [True, False, False]
#   # index_list = [0, 2]
#   # not_list(bool_list, index_list) -> [False, False, True]
#   #
#   #After calling not_list, the booleans at indices 0 and 2
#   #have been switched.
#   #
#   #Note that it may be the case that the same index is present
#   #in the second twice. If this happens, you should switch the
#   #boolean at that index twice. For example:
#   #
#   # bool_list = [True, False, False]
#   # index_list = [0, 2, 2]
#   # not_list(bool_list, index_list) -> [False, False, False]
#   #
#   #2 is in index_list twice, so the boolean at index 2 is
#   #switched twice: False to True, then True back to False.
#   #
#   #Hint: Remember you can change a list in place! You don't
#   #need to create a new list. a_list[1] = False, for example,
#   #changes the item in a_list at index 1 to False.
# ---- model response below: edit from here ----
def not_list(bool_list, index_list):
    """
    Switch the values of all the booleans located at the given indices in the list.

    Args:
        bool_list (list): A list of booleans.
        index_list (list): A list of integers representing indices for the bool_list.

    Returns:
        None
    """
    for index in index_list:
        # Use the modulus operator to handle cases where an index is out of range
        bool_list[index % len(bool_list)] = not bool_list[index % len(bool_list)]