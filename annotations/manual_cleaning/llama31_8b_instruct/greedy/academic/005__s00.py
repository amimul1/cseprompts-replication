# ================= CSEPrompts manual cleaning =================
# task: academic/005 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00,
#   lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you
#   had a program that could tell you what to eat when?
#   
#   Implement a program that prompts the user for a time and outputs whether it’s breakfast time,
#   lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume
#   that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each
#   meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime
#   in between, it’s time for breakfast.
#   
#   Structure your program per the below, wherein convert is a function (that can be called by main)
#   that converts time, a str in 24-hour format, to the corresponding number of hours as a float.
#   For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5
#   (i.e., 7.5 hours).
# ---- model response below: edit from here ----
### Meal Time Program
def convert(time: str) -> float:
    """
    Convert time from 24-hour format to a float representing the number of hours.

    Args:
    time (str): Time in 24-hour format (e.g., "7:30" or "12:00").

    Returns:
    float: The time in hours as a float (e.g., 7.5 or 12.0).
    """
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60


def meal_time(time: str) -> None:
    """
    Determine the meal based on the given time.

    Args:
    time (str): Time in 24-hour format (e.g., "7:30" or "12:00").
    """
    time_in_hours = convert(time)
    if 7.0 <= time_in_hours <= 8.0:
        print("It's breakfast time!")
    elif 12.0 <= time_in_hours <= 13.0:
        print("It's lunch time!")
    elif 18.0 <= time_in_hours <= 19.0:
        print("It's dinner time!")


def main():
    """
    Main function to get user input and determine the meal.
    """
    time = input("Enter the time (in 24-hour format, e.g., 7:30 or 12:00): ")
    meal_time(time)


if __name__ == "__main__":
    main()