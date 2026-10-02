# ================= CSEPrompts manual cleaning =================
# task: academic/046 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   num = 3
#   
#   #-----------------------------------------------------------
#   #You may modify the lines of code above, but don't move them!
#   #When you Submit your code, we'll change these lines to
#   #assign different values to the variables.
#   
#   #Write some code that calculates the cube of the number
#   #given by num. Then, print that number num^2 (num squared)
#   #times in a row, with no spaces or line breaks in between.
#   #
#   #For example, if num is 3, then your code would print:
#   #
#   # 272727272727272727
#   #
#   #That 27 9 times. 3 squared is 9, 3 cubed is 27, and so
#   #it prints 27 9 times.
#   #
#   #Note: these directions are slightly different from the
#   #preview we posted! You should be printing num^3 num^2
#   #times, not printing num^2 num^3 times.
# ---- model response below: edit from here ----
num = 3

# Calculate the cube of num
cube = num ** 3

# Calculate num squared
squared = num ** 2

# Print the cube num squared times
print(cube * '27' * squared)