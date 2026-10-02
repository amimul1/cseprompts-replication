# ================= CSEPrompts manual cleaning =================
# task: academic/062 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called check_date. check_date should
#   #require two positional parameters: a string representing
#   #the name of a month, and an integer representing a date.
#   #check_date should also have a keyword parameter called
#   #is_leap_year, assumed to be False, representing whether or
#   #not it's a leap year.
#   #
#   #Return True if the date is a valid calendar date. Return
#   #False if it is not. A date may not be a valid calendar
#   #date if the month isn't a real month, or if that date does
#   #not exist for that month. You can see some examples at the
#   #end of this file.
#   #
#   #Remember: 30 days has September, April, June, and November.
#   #All the rest have 31, except February, which has 28, until
#   #Leap Year gives it 29.
#   #
#   #You may assume that day will be greater than 0 (you don't
#   #need to check negative or zero values for day).
# ---- model response below: edit from here ----
def check_date(month, day, is_leap_year=False):
    """
    Checks if a given date is a valid calendar date.

    Args:
        month (str): The name of the month.
        day (int): The day of the month.
        is_leap_year (bool, optional): Whether it's a leap year. Defaults to False.

    Returns:
        bool: True if the date is a valid calendar date, False otherwise.
    """

    # Define the number of days in each month
    days_in_month = {
        "January": 31,
        "February": 28 if not is_leap_year else 29,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    # Check if the month is valid
    if month not in days_in_month:
        return False

    # Check if the day is valid for the given month
    if day > days_in_month[month]:
        return False

    # If we've reached this point, the date is valid
    return True