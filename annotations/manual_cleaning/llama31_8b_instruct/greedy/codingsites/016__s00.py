# ================= CSEPrompts manual cleaning =================
# task: codingsites/016 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function to check if the given year is leap or not.
# ---- model response below: edit from here ----
def is_leap_year(year: int) -> bool:
    """
    Checks if a given year is a leap year.

    A year is a leap year if it is perfectly divisible by 4 except for end-of-century years which must be divisible by 400. 
    This means that the year 2000 was a leap year, although 1900 was not.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:  # If the year is divisible by 4, it's a leap year unless...
        if year % 100 == 0:  # ...it's a century year
            if year % 400 == 0:  # ...which is a leap year if it's also divisible by 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False
