# ================= CSEPrompts manual cleaning =================
# task: codingsites/015 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Read an integer N. For all non-negative integers i<N, print i^2.
# ---- model response below: edit from here ----
def print_squares(N):
    """
    Prints the squares of all non-negative integers less than N.
    
    Args:
        N (int): The upper limit (exclusive).
    """
    for i in range(N):
        print(i ** 2)