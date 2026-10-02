# ================= CSEPrompts manual cleaning =================
# task: academic/047 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   current_day = 31
#   current_month = 5
#   current_year = 2018
#   birth_day = 19
#   birth_month = 12
#   birth_year = 1990
#   
#   #You may modify the lines of code above, but don't move them!
#   #When you Submit your code, we'll change these lines to
#   #assign different values to the variables.
#   
#   #Given the current date and birth date held by the variables
#   #above, calculate and print this person's current age. Note
#   #that if their birth date has not yet passed this year, your
#   #result would be one less than if it has.
#   #
#   #For example, with the variables given above, the person
#   #would turn 28 on December 12th, 2018. So, as of May 31st,
#   #2018, they are 27.
# ---- model response below: edit from here ----
from datetime import datetime

# Given the current date and birth date
current_day = 31
current_month = 5
current_year = 2018
birth_day = 19
birth_month = 12
birth_year = 1990

# Create a datetime object for the current date
current_date = datetime(current_year, current_month, current_day)

# Create a datetime object for the birth date
birth_date = datetime(birth_year, birth_month, birth_day)

# If the birth date has not yet passed this year, subtract one from the age
if birth_date.year == current_year:
    age = current_date.month < birth_month or (current_date.month == birth_month and current_date.day < birth_day)
    age = 0 if age else 1
else:
    age = current_year - birth_year

print("The person's current age is:", age)