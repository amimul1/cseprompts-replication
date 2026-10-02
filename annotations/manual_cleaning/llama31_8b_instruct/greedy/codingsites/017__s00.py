# ================= CSEPrompts manual cleaning =================
# task: codingsites/017 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Without using any string methods, try to print the following: 123...N
# ---- model response below: edit from here ----
def print_numbers(n):
    """
    Prints numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the range.
    """
    num = 1
    while num <= n:
        print(num, end=' ')
        num += 1
