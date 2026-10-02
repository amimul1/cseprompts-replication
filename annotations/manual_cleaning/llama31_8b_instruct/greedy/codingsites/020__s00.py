# ================= CSEPrompts manual cleaning =================
# task: codingsites/020 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create a function that takes a number as an argument, increments the number by +1 and returns
#   the result.
# ---- model response below: edit from here ----
def increment_number(num: int) -> int:
    """
    Increments a given number by 1.

    Args:
        num (int): The number to be incremented.

    Returns:
        int: The incremented number.
    """
    return num + 1