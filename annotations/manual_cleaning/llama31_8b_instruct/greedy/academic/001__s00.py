# ================= CSEPrompts manual cleaning =================
# task: academic/001 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   implement a program that prompts the user for the answer to the Great Question of Life, the
#   Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two
#   or forty two. Otherwise output No
# ---- model response below: edit from here ----
def ultimate_answer():
    """
    Prompts the user for the answer to the Great Question of Life, the Universe and Everything.
    Outputs 'Yes' if the user inputs 42 or (case-insensitively) 'forty-two' or 'forty two'. Otherwise outputs 'No'.
    """
    user_input = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

    # Convert user input to lower case for case-insensitive comparison
    user_input = user_input.lower()

    # Check if user input matches the ultimate answer
    if user_input in ['42', 'forty-two', 'forty two']:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    ultimate_answer()
