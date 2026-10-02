# ================= CSEPrompts manual cleaning =================
# task: academic/055 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   driver_speed = 57
#   speed_limit = 55
#   school_zone = True
#   
#   #You may modify the lines of code above, but don't move them!
#   #When you Submit your code, we'll change these lines to
#   #assign different values to the variables.
#   
#   #Write a conditional that decides the price of a speed ticket
#   #depending on the driver's speed, the speed limit, and
#   #whether or not they were in a school zone.
#   #
#   #The reasoning that determines the price of the ticket is:
#   #
#   # - $100 for speeding at all (any instance where driver_speed
#   #   is greater than speed limit).
#   # - $10 dollars per mile over the speed limit the driver was
#   #   going.
#   # - 2x the value otherwise if the violation occurred in a
#   #   school zone, as represented by the value of school_zone.
#   #
#   #Print the cost of the speeding ticket. If the driver was not
#   #speeding, print $0.
#   #
#   #Under the original values above, this should print $240:
#   #$100 for speeding, $20 for going 2mph above the speed limit,
#   #and x2 for it occurring in a school zone.
# ---- model response below: edit from here ----
driver_speed = 57
speed_limit = 55
school_zone = True

# Calculate the speed difference
speed_diff = driver_speed - speed_limit

# Check if the driver was speeding
if speed_diff > 0:
    # Calculate the price of the ticket
    price = 100 + (speed_diff - 1) * 10  # subtract 1 to avoid double counting the initial $100
    # If the violation occurred in a school zone, double the price
    if school_zone:
        price *= 2
    print(f"The cost of the speeding ticket is: ${price}")
else:
    print("The driver was not speeding. The cost of the ticket is: $0")