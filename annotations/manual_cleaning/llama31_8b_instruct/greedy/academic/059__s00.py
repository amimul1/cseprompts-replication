# ================= CSEPrompts manual cleaning =================
# task: academic/059 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called find_weight. find_weight should
#   #take one positional parameter, a float that represents
#   #the mass of an object in kilograms. It should return the
#   #weight of the object.
#   #
#   #You should assume that the planet is earth and that the
#   #acceleration due to gravity is 9.81; however, find_weight
#   #should also have a keyword parameter called gravity that
#   #allows this value to be overriden to calculate an
#   #object's weight on other planets.
#   #
#   #Remember, the formula for weight is mass * gravity. If
#   #you find Python is making rounding errors, try reversing
#   #the order in which you multiply the numbers.
# ---- model response below: edit from here ----
def find_weight(mass, gravity=9.81):
    """
    Calculate the weight of an object given its mass and the acceleration due to gravity.

    Args:
        mass (float): The mass of the object in kilograms.
        gravity (float, optional): The acceleration due to gravity. Defaults to 9.81 (Earth's gravity).

    Returns:
        float: The weight of the object in Newtons.
    """
    return mass * gravity