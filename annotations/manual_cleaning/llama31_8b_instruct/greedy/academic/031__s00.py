# ================= CSEPrompts manual cleaning =================
# task: academic/031 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a program that uses input to prompt a user for their name and then welcomes them. Note
#   that input will pop up a dialog box. Enter Sarah in the pop-up box when you are prompted so your
#   output will match the desired output.
# ---- model response below: edit from here ----
# Get the user's name
name = input("Please enter your name: ")

# Welcome the user
print(f"Hello, {name}! It's nice to meet you.")