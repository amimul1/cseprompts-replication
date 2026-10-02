# ================= CSEPrompts manual cleaning =================
# task: academic/042 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   principal = 40000
#   rate = 0.05
#   years = 5
#   goal = 50000
#   
#   #You may modify the lines of code above, but don't move them!
#   #When you Submit your code, we'll change these lines to
#   #assign different values to the variables.
#   
#   #Last problem, we calculated how much money a person would
#   #have to invest to reach a certain savings goal. Now, let's
#   #modify that to instead take a principal, interest rate,
#   #number of years, and savings goal, and report whether or not
#   #the person will meet their savings goal.
#   #
#   #Add some code below that will calculate whether the
#   #investment described by the values above will meet the given
#   #goal. If it will, print True. If it will not, print False.
#   #
#   #As a reminder, the formula for the value of an account after
#   #a given time (in number of years) is:
#   #
#   #  Current Value = principal * e ^ (rate * number of years)
#   #
#   #Remember, you can access e using math.e as long as you don't
#   #change the next line. You don't need to worry about rounding
#   #on this problem.
# ---- model response below: edit from here ----
import math

principal = 40000
rate = 0.05
years = 5
goal = 50000

# Calculate the current value of the account
current_value = principal * math.e ** (rate * years)

# Check if the current value meets the goal
if current_value >= goal:
    print(True)
else:
    print(False)