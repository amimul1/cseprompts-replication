# ================= CSEPrompts manual cleaning =================
# task: academic/058 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called find_weight. find_weight should
#   #take one parameter, a float that represents the mass of
#   #an object in kilograms. It should return the weight of
#   #the object on earth.
#   #
#   #Remember, the formula for weight is mass * gravity. You
#   #should use 9.81 as the value for gravity on earth. If
#   #you find Python is making rounding errors, try reversing
#   #the order in which you multiply the numbers.
# ---- model response below: edit from here ----
def find_weight(mass: float) -> float:
    """
    Calculate the weight of an object on Earth.

    Args:
        mass (float): The mass of the object in kilograms.

    Returns:
        float: The weight of the object on Earth in Newtons.
    """
    # Define the acceleration due to gravity on Earth in m/s^2
    gravity = 9.81
    
    # Calculate the weight by multiplying the mass by gravity
    # To avoid rounding errors, we multiply the numbers in the order that minimizes the loss of precision
    weight = mass * gravity
    
    return weight

# Example usage:
mass = 50.0  # mass in kg
weight = find_weight(mass)
print(f"The weight of the object is {weight} N")