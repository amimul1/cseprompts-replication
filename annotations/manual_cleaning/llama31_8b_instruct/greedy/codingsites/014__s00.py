# ================= CSEPrompts manual cleaning =================
# task: codingsites/014 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Read two integers and print two lines. The first line should contain integer division, a//b. The
#   second line should contain float division, a/b.
# ---- model response below: edit from here ----
# Read two integers
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Perform integer division
integer_division = a // b

# Perform float division
float_division = a / b

# Print the results
print("Integer division:", integer_division)
print("Float division:", float_division)