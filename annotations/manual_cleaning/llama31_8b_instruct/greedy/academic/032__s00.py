# ================= CSEPrompts manual cleaning =================
# task: academic/032 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#   Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You
#   should use input to read a string and float() to convert the string to a number. Do not worry
#   about error checking or bad user data.
# ---- model response below: edit from here ----
# Prompt the user for hours and rate per hour
hours = input("Enter hours worked: ")
rate = input("Enter rate per hour: ")

# Convert the input strings to floats
hours = float(hours)
rate = float(rate)

# Calculate the gross pay
gross_pay = hours * rate

# Print the result
print(f"Gross pay: ${gross_pay:.2f}")