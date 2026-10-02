# ================= CSEPrompts manual cleaning =================
# task: academic/054 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   int1 = 7
#   int2 = 5
#   
#   #You may modify the lines of code above, but don't move them!
#   #When you Submit your code, we'll change these lines to
#   #assign different values to the variables.
#   
#   #Write a conditional that will print one of the following
#   #messages:
#   #
#   # - If the value of int1 is greater than the value of int2,
#   #   print "int1 is greater" (without the quotes).
#   # - If the value of int2 is greater than the value of int1,
#   #   print "int2 is greater" (without the quotes).
#   # - If the two values are equal, print "int1 and int2 are
#   #   equal" (without the quotes).
#   #
#   #With the initial values above, this should print "int1 is
#   #greater".
# ---- model response below: edit from here ----
int1 = 7
int2 = 5

if int1 > int2:
    print("int1 is greater")
elif int2 > int1:
    print("int2 is greater")
else:
    print("int1 and int2 are equal")