# ================= CSEPrompts manual cleaning =================
# task: academic/082 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #-----------------------------------------------------------
#   #Write a function called no_you_pick. no_you_pick should
#   #have two parameters. The first parameter is a dictionary
#   #where the keys are restaurant names and the values are lists
#   #of attributes of those restaurants as strings, such as
#   #"vegetarian", "vegan", and "gluten-free".
#   #
#   #The second parameter is a list of strings representing of
#   #necessary attributes of the restaurant you select.
#   #
#   #Return a list of restaurants from the dictionary who each
#   #contain all the diet restrictions listed in the list,
#   #sorted alphabetically. If there are no restaurants that
#   #meet all the restrictions, return the string "Sorry, no
#   #restaurants meet your restrictions". Types of diet
#   #restrictions that exist in this question's universe are:
#   #vegetarian, vegan, kosher, gluten-free, dairy-free
#   #
#   #For example:
#   #grading_scale = {"blossom": ["vegetarian", "vegan", "kosher", "gluten-free", "dairy-free"], \
#   #                 "jacob's pickles": ["vegetarian", "gluten-free"], \
#   #                 "sweetgreen": ["vegetarian", "vegan", "gluten-free", "kosher"]}
#   #guests_diet = ["dairy-free"]
#   #no_you_pick(grading_scale, guests_diet) -> ["blossom"]
# ---- model response below: edit from here ----
def no_you_pick(grading_scale, guests_diet):
    """
    Returns a list of restaurants from the dictionary that meet all the diet restrictions.

    Args:
        grading_scale (dict): A dictionary where keys are restaurant names and values are lists of attributes.
        guests_diet (list): A list of necessary attributes of the restaurant.

    Returns:
        list: A list of restaurants that meet all the diet restrictions, sorted alphabetically.
               If no restaurants meet the restrictions, returns "Sorry, no restaurants meet your restrictions".
    """
    # Filter restaurants that meet all the diet restrictions
    suitable_restaurants = {restaurant: attributes for restaurant, attributes in grading_scale.items() 
                          if all(attribute in attributes for attribute in guests_diet)}
    
    # If no restaurants meet the restrictions, return the message
    if not suitable_restaurants:
        return "Sorry, no restaurants meet your restrictions"
    
    # Return the list of suitable restaurants, sorted alphabetically
    return sorted(suitable_restaurants.keys())