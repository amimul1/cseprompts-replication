# ================= CSEPrompts manual cleaning =================
# task: codingsites/082 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   We add a Leap Day on February 29, almost every four years. The leap day is an extra, or
#   intercalary day and we add it to the shortest month of the year, February. In the Gregorian
#   calendar three criteria must be taken into account to identify leap years: The year can be
#   evenly divided by 4, is a leap year, unless: The year can be evenly divided by 100, it is NOT a
#   leap year, unless: The year is also evenly divisible by 400. Then it is a leap year. Write
#   function to determine whether a year is a leap year.
# ---- model response below: edit from here ----
def is_leap_year(year: int) -> bool:
    """
    Determine whether a year is a leap year.

    A year is a leap year if it meets the following conditions:
    1. The year can be evenly divided by 4.
    2. If the year can be evenly divided by 100, it is NOT a leap year.
    3. However, if the year is also evenly divisible by 400, it is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)