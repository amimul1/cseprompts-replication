# ================= CSEPrompts manual cleaning =================
# task: academic/060 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   list_sum = 7
#   list_count = 0
#   
#   #You may modify the lines of code above, but don't move them!
#   #When you Submit your code, we'll change these lines to
#   #assign different values to the variables.
#   #
#   #The variables above give the sum of all numbers in a list,
#   #and the count of how many numbers were in the list. Your
#   #goal is to find their average.
#   #
#   #However, if list_count is 0, then we can't divide list_sum
#   #by list_count. In this case, you should print "Can't divide
#   #by zero!" Otherwise, you should print the average.
#   #
#   #Note that you may not use any conditionals in your answer.
#   #Note also that you should not assume that every error that
#   #occurs is a divide-by-zero error: any other errors should
#   #not be caught.
# ---- model response below: edit from here ----
list_sum = 7
list_count = 0

average = list_sum / list_count if list_count != 0 else "Can't divide by zero!"
print(average)