# ================= CSEPrompts manual cleaning =================
# task: academic/074 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called average_rainfall. average_rainfall
#   #should have one parameter, a list of integers. The list
#   #represents daily rainfall measurements for a certain area.
#   #
#   #However, at some point in the list, there will be a -1.
#   #This indicates that you should stop averaging, and ignore
#   #any subsequent values.
#   #
#   #For example:
#   #
#   #average_rainfall([1, 2, 3, 4, 5, -1, 6, 7]) -> 3.0
#   #
#   #The function would only average 1, 2, 3, 4, and 5, and
#   #ignore any values after the -1.
#   #
#   #You may assume all the items in the list are integers,
#   #that -1 is guaranteed to occur somewhere in the list,
#   #and that -1 will not be the first item in the list.
# ---- model response below: edit from here ----
def average_rainfall(rainfall_list):
    """
    Calculate the average rainfall up to the point where the rainfall measurement is -1.

    Args:
        rainfall_list (list): A list of integers representing daily rainfall measurements.

    Returns:
        float: The average rainfall up to the point where the rainfall measurement is -1.
    """
    # Filter out the rainfall measurements up to the point where the rainfall measurement is -1
    rainfall_sum = sum(rainfall for rainfall in rainfall_list if rainfall != -1)
    
    # Count the number of rainfall measurements up to the point where the rainfall measurement is -1
    rainfall_count = sum(1 for rainfall in rainfall_list if rainfall != -1)
    
    # Check if there are any rainfall measurements
    if rainfall_count == 0:
        return 0.0  # Return 0.0 if there are no rainfall measurements
    
    # Calculate the average rainfall
    average = rainfall_sum / rainfall_count
    
    return average