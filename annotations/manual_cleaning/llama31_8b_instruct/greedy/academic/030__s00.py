# ================= CSEPrompts manual cleaning =================
# task: academic/030 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a program that uses a print function to say 'hello world' as shown in 'Desired Output'.
# ---- model response below: edit from here ----
def main():
    """
    Prints "Hello, World!" to the console.
    """
    print("Hello, World!")

if __name__ == "__main__":
    main()
