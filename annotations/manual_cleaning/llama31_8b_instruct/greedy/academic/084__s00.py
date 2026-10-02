# ================= CSEPrompts manual cleaning =================
# task: academic/084 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #You are going through your refrigerator at home and trying to determine whether you have the
#   proper ingredients to cook a meal.
#   #
#   #Write a function called food_at_home. food_at_home should have one parameter, a list of foods
#   in your house as strings. In order to cook a meal, the list must contain "cooking oil" and at
#   least one other item. If this criteria is not met, return the string "I guess it's pizza
#   tonight". If you do have cooking oil and at least one other food, return the string, "You do
#   have food, your options are ... or ... or ...", where the ...s are replaced by the food names in
#   the list in the order in which they appear. "cooking oil" should not be one of the foods listed
#   under options.
#   #
#   #For example:
#   #food_list = ["chicken", "mixed veggies", "greens", "beans", "corn", "cooking oil"]
#   #food_at_home(food_list) -> "You do have food, your options are chicken or mixed veggies or
#   greens or beans or corn"
# ---- model response below: edit from here ----
### Food Availability Checker Function
def food_at_home(food_list):
    """
    Checks if you have the necessary ingredients to cook a meal at home.

    Args:
        food_list (list): A list of foods in your house as strings.

    Returns:
        str: A message indicating whether you have the necessary ingredients and your options.
    """
    # Check if cooking oil is in the list
    if "cooking oil" not in food_list:
        return "I guess it's pizza tonight"

    # Remove "cooking oil" from the list
    food_list.remove("cooking oil")

    # Check if there are at least two other foods in the list
    if len(food_list) < 2:
        return "I guess it's pizza tonight"

    # Join the remaining foods into a string with " or " in between
    options = " or ".join(food_list)

    # Return the message with the options
    return f"You do have food, your options are {options}"