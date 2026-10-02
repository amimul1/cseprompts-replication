# ================= CSEPrompts manual cleaning =================
# task: codingsites/012 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given an integer, n, perform the following conditional actions: If n is odd, print Weird. If n
#   is even and in the inclusive range of 2 to 5, print Not Weird. If n is even and in the inclusive
#   range of 6 to 20, print Weird. If n is even and greater than 20, print Not Weird.
# ---- model response below: edit from here ----
def check_weird(n):
    """
    Prints whether a given number is Weird or Not Weird based on the specified conditions.

    Args:
        n (int): The number to check.

    Returns:
        None
    """
    if n % 2 != 0:  # Check if n is odd
        print("Weird")
    elif 2 <= n <= 5:  # Check if n is even and in the range 2 to 5
        print("Not Weird")
    elif 6 <= n <= 20:  # Check if n is even and in the range 6 to 20
        print("Weird")
    else:  # n is even and greater than 20
        print("Not Weird")