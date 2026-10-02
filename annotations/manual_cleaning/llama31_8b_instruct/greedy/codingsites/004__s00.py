# ================= CSEPrompts manual cleaning =================
# task: codingsites/004 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Define a function, random_number, that takes no parameters. The function must generate a random
#   integer between 1 and 100.
# ---- model response below: edit from here ----
import random

def random_number():
    """
    Generates a random integer between 1 and 100.
    
    Returns:
        int: A random integer between 1 and 100.
    """
    return random.randint(1, 100)