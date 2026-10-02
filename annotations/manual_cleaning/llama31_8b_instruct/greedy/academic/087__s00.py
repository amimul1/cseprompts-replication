# ================= CSEPrompts manual cleaning =================
# task: academic/087 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called check_value. check_value should
#   #take as input two parameters: a dictionary and a string.
#   #Both the keys and the values in the dictionary will be
#   #strings. The string parameter will be the key to look up in
#   #the dictionary.
#   #
#   #check_value should look up the string in the dictionary and
#   #get its value. Its current value will always be a string;
#   #however, check_value should try to convert it to an integer
#   #and a float, then return a message indicating the success
#   #of those conversions:
#   #
#   # - If the key is not found in the dictionary, check_value
#   #   should return the string: "Not found!"
#   # - If the value corresponding to the key can be converted
#   #   to an integer, check_value should return the string:
#   #   "Integer!"
#   # - Otherwise, if the value corresponding to the key can be
#   #   converted to a float, check_value should return the
#   #   string: "Float!"
#   # - Otherwise, check_value should return the string:
#   #   "String!"
#   #
#   #You do not need to check for any other types. We suggest
#   #using error handling to try to convert the values to the
#   #corresponding data types.
#   #
#   #For example, given this dictionary:
#   #
#   # d = {"k1": "1.1", "k2": "1", "k3": "1.4.6", "k4": "a"}
#   #
#   #Here are some calls and their results:
#   #
#   # - check_value(d, "k1") -> "Float!"
#   # - check_value(d, "k2") -> "Integer!"
#   # - check_value(d, "k3") -> "String!"
#   # - check_value(d, "k4") -> "String!"
#   # - check_value(d, "k5") -> "Not found!"
#   #
#   #Hint: The error that arises when trying to convert a
#   #string to a type it can't convert to (e.g. "ABC" to a
#   #float) is a ValueError. The error that arises when
#   #trying to access a key that doesn't exist in a
#   #dictionary is a KeyError.
# ---- model response below: edit from here ----
def check_value(dictionary, key):
    """
    This function checks the value associated with a given key in a dictionary.
    It tries to convert the value to an integer and a float, then returns a message
    indicating the success of those conversions.

    Args:
        dictionary (dict): A dictionary with string keys and values.
        key (str): The key to look up in the dictionary.

    Returns:
        str: A message indicating the type of the value associated with the key.
    """

    # First, we try to get the value associated with the key from the dictionary
    try:
        value = dictionary[key]
    except KeyError:
        # If the key is not found in the dictionary, we return "Not found!"
        return "Not found!"

    # We try to convert the value to an integer
    try:
        int(value)
        # If the conversion is successful, we return "Integer!"
        return "Integer!"
    except ValueError:
        # If the conversion to integer fails, we try to convert the value to a float
        try:
            float(value)
            # If the conversion is successful, we return "Float!"
            return "Float!"
        except ValueError:
            # If the conversion to float also fails, we return "String!"
            return "String!"