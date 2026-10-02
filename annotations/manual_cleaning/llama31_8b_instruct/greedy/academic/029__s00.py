# ================= CSEPrompts manual cleaning =================
# task: academic/029 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Assuming there are 365 days in a year, there are 525600 minutes in that same year (because there
#   are 24 hours in a day and 60 minutes in an hour). But how many minutes are there in two or more
#   years? Well, it depends on how many of those are leap years with 366 days, per the Gregorian
#   calendar, as some of them could have 1440 additional minutes. In fact, how many minutes has it
#   been since you were born? Well, that, too, depends on how many leap years there have been since!
#   There is an algorithm for such, but let’s not reinvent that wheel. Let’s use a library instead.
#   Fortunately, Python comes with a datetime module that has a class called date that can help, per
#   docs.python.org/3/library/datetime.html#date-objects.
#   
#   In a file called seasons.py, implement a program that prompts the user for their date of birth
#   in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest
#   integer, using English words instead of numerals, just like the song from Rent, without any and
#   between words. Since a user might not know the time at which they were born, assume, for
#   simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that
#   the current time is also midnight. In other words, even if the user runs the program at noon,
#   assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s
#   date, per docs.python.org/3/library/datetime.html#datetime.date.today.
# ---- model response below: edit from here ----
from datetime import date

def get_age_in_minutes(birth_date):
    """
    Calculate the age in minutes since birth date.

    Args:
        birth_date (date): The date of birth.

    Returns:
        int: The age in minutes.
    """
    today = date.today()
    age = today - birth_date
    return age.days * 24 * 60

def get_age_in_words(minutes):
    """
    Convert minutes to words.

    Args:
        minutes (int): The age in minutes.

    Returns:
        str: The age in words.
    """
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if minutes < 10:
        return ones[minutes]
    elif minutes < 20:
        return teens[minutes - 10]
    elif minutes < 100:
        return tens[minutes // 10] + (" " + ones[minutes % 10] if minutes % 10 != 0 else "")
    elif minutes < 1000:
        return ones[minutes // 100] + " hundred" + ((" and " + get_age_in_words(minutes % 100)) if minutes % 100 != 0 else "")

def main():
    birth_date_str = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birth_date = date(int(birth_date_str.split("-")[0]), int(birth_date_str.split("-")[1]), int(birth_date_str.split("-")[2]))
        age_in_minutes = get_age_in_minutes(birth_date)
        age_in_words = get_age_in_words(age_in_minutes)
        print(f"You are {age_in_words} minutes old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()