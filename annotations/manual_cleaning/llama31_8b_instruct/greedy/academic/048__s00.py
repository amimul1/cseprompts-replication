# ================= CSEPrompts manual cleaning =================
# task: academic/048 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Imagine you're writing the software that controls the speed
#   #of a ceiling fan. The user changes the fan's speed by
#   #pulling a string. Pulling the string increases the fan's =
#   #speed by 1, unless it's already at the maximum speed. If
#   #it's already at the maximum speed, it changes the speed
#   #back to 0.
#   #
#   #Write a function called pullString. pullString should take
#   #two parameters: a current speed, and a maximum speed, both
#   #integers. pullString should return the new fan speed
#   #according to the reasoning above.
#   
#   #You may assume that the input will be integers. You should
#   #also assume that the fan's speed *can* equal the maximum
#   #speed, but it *cannot* exceed the maximum speed. You may
#   #thus assume that you will never be given a currentSpeed
#   #higher than maxSpeed.
# ---- model response below: edit from here ----
### Ceiling Fan Speed Controller
def pull_string(current_speed, max_speed):
    """
    This function controls the speed of a ceiling fan based on the given current speed and maximum speed.
    
    Args:
        current_speed (int): The current speed of the fan.
        max_speed (int): The maximum speed of the fan.
    
    Returns:
        int: The new speed of the fan after pulling the string.
    """
    
    # If the current speed is equal to the maximum speed, reset it to 0
    if current_speed == max_speed:
        return 0
    # Otherwise, increase the current speed by 1
    else:
        return current_speed + 1