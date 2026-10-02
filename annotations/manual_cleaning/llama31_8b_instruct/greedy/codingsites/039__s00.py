# ================= CSEPrompts manual cleaning =================
# task: codingsites/039 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Use the 'format' method to print out the specified string with the correct values inserted
# ---- model response below: edit from here ----

# Define a string with placeholders
name = "John"
age = 30

# Use the format() method to insert values into the string
greeting = "Hello, my name is {} and I am {} years old.".format(name, age)

# Print the formatted string
print(greeting)
