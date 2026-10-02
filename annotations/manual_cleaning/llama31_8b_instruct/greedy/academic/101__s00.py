# ================= CSEPrompts manual cleaning =================
# task: academic/101 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called add_to_dictionary. add_to_dictionary
#   #should have three parameters: a dictionary, a potential new
#   #key, and a potential new value.
#   #
#   #add_to_dictionary should add the given key and value to the
#   #dictionary if the key is of a legal type to be used as a
#   #dictionary key.
#   #
#   #If the key is a legal type to be used as a dictionary key,
#   #return the resultant dictionary.
#   #
#   #If the key is _not_ a legal type to be used as a dictionary
#   #key, return the string "Error!"
#   #
#   #Remember, only immutable types can be used as dictionary
#   #keys. If you don't remember which types are immutable or
#   #how to check a value's type, don't fret: there's a way
#   #to do this without checking them directly!
# ---- model response below: edit from here ----
def add_to_dictionary(dictionary, key, value):
    """
    Adds a key-value pair to a dictionary if the key is of a legal type to be used as a dictionary key.

    Args:
        dictionary (dict): The dictionary to add the key-value pair to.
        key: The potential new key.
        value: The potential new value.

    Returns:
        dict: The resultant dictionary if the key is a legal type, otherwise "Error!".
    """
    # Check if the key is of a type that can be used as a dictionary key
    if isinstance(key, (str, int, float, tuple, frozenset, bytes, bool)):
        # If the key is a legal type, add the key-value pair to the dictionary
        dictionary[key] = value
        return dictionary
    else:
        # If the key is not a legal type, return "Error!"
        return "Error!"