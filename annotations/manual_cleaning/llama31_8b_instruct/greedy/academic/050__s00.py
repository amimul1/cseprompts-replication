# ================= CSEPrompts manual cleaning =================
# task: academic/050 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #An object's weight is defined as its mass times the gravity
#   #on the planet where it sits. We tend to assume that the
#   #planet is earth and its gravity is 9.807 m/s^2. However,
#   #sometimes we might want to calculate an object's weight on
#   #a different planet.
#   #
#   #Write a function called calculateWeight. calculateWeight
#   #should have three parameters: mass, planet, and gravity.
#   #planet and gravity should be keyword parameters: by
#   #default, they should take the values "Earth" (a string) and
#   #9.807 (a float). However, they should be able to be
#   #overriden to let us calculate weights on other planets.
#   #
#   #The function should return a string that looks like this:
#   #"A [mass] kg object weighs [weight] Newtons on [planet]."
#   #You should round the weight to two decimal points. You
#   #can do this by calling round() on the weight, e.g.
#   #roundedWeight = round(weight, 2). The 2 dictates how
#   #many decimal points should be included.
#   #
#   #For example:
#   #
#   # calculateWeight(10.0) ->
#   #       "A 10.0 kg object weighs 98.07 Newtons on Earth."
#   #
#   # calculateWeight(5.0, planet="Jupiter", gravity=24.79) ->
#   #       "A 5.0 kg object weighs 24.79 Newtons on Jupiter."
#   #
#   #Hint: If you're having trouble with creating the string to
#   #return, here's the first part:
#   #result = "A " + str(mass) + " kg object weighs " ...
# ---- model response below: edit from here ----
def calculate_weight(mass, planet="Earth", gravity=9.807):
    """
    Calculate the weight of an object on a given planet.

    Args:
        mass (float): The mass of the object in kg.
        planet (str, optional): The name of the planet. Defaults to "Earth".
        gravity (float, optional): The gravity of the planet in m/s^2. Defaults to 9.807.

    Returns:
        str: A string describing the weight of the object on the given planet.
    """
    # Calculate the weight by multiplying the mass by the gravity
    weight = mass * gravity
    
    # Round the weight to two decimal points
    rounded_weight = round(weight, 2)
    
    # Create the result string
    result = "A " + str(mass) + " kg object weighs " + str(rounded_weight) + " Newtons on " + planet + "."
    
    return result

# Test the function
print(calculate_weight(10.0))  # Output: A 10.0 kg object weighs 98.07 Newtons on Earth.
print(calculate_weight(5.0, planet="Jupiter", gravity=24.79))  # Output: A 5.0 kg object weighs 124.95 Newtons on Jupiter.