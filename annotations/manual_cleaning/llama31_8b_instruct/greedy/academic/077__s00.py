# ================= CSEPrompts manual cleaning =================
# task: academic/077 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called complete_profile. complete_profile
#   #will take as input a dictionary. This dictionary will have
#   #four keys: first, middle, last, and title. The function
#   #should return a dictionary with those four keys, and three
#   #more: name, full_name, short_name. The values for those
#   #keys should be:
#   #
#   # - name: the first and last name, separated by a space
#   # - full_name: the title, first, middle, and last names,
#   #   with a space between each pair of strings
#   # - short_name: the first letter of the first name, a space,
#   #   and their last name
#   #
#   #For example:
#   #
#   # complete_profile({"first": "David", "middle": "Andrew",
#   #                   "last": "Joyner", "title": "Dr."})
#   #
#   # would return:
#   #
#   # {"first": "David", "middle": "Andrew", "last": "Joyner",
#   #  "title": "Dr.", "name": "David Joyner",
#   #  "full_name": "Dr. David Andrew Joyner",
#   #  "short_name": "D Joyner"}
#   #
#   #You may either modify the dictionary that is passed in,
#   #or create a new one. Either way, make sure to return the
#   #dictionary at the end of the function.
# ---- model response below: edit from here ----
def complete_profile(profile):
    """
    This function takes a dictionary with four keys: first, middle, last, and title.
    It returns a dictionary with the original four keys and three additional keys: name, full_name, and short_name.
    
    The values for the additional keys are:
    - name: the first and last name, separated by a space
    - full_name: the title, first, middle, and last names, with a space between each pair of strings
    - short_name: the first letter of the first name, a space, and their last name
    
    :param profile: A dictionary with keys 'first', 'middle', 'last', and 'title'
    :return: A dictionary with the original keys and the three additional keys
    """
    
    # Create a copy of the input dictionary to avoid modifying it directly
    profile = profile.copy()
    
    # Calculate the name by concatenating the first and last names
    profile['name'] = profile['first'] + ' ' + profile['last']
    
    # Calculate the full name by concatenating the title, first, middle, and last names
    profile['full_name'] = profile['title'] + ' ' + profile['first'] + ' ' + profile['middle'] + ' ' + profile['last']
    
    # Calculate the short name by taking the first letter of the first name and the last name
    profile['short_name'] = profile['first'][0] + ' ' + profile['last']
    
    # Return the updated dictionary
    return profile