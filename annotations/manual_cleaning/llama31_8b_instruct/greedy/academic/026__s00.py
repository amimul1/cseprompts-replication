# ================= CSEPrompts manual cleaning =================
# task: academic/026 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock.
#   Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00
#   PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an
#   abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).
#   
#   Conversion Table
#   Just as “12:00 AM” in 12-hour format would be “00:00” in 24-hour format, so would “12:01 AM”
#   through “12:59 AM” be “00:01” through “00:59”, respectively.
#   
#   12-Hour
#   24-Hour
#   12:00 AM        00:00
#   1:00 AM 01:00
#   2:00 AM 02:00
#   3:00 AM 03:00
#   4:00 AM 04:00
#   5:00 AM 05:00
#   6:00 AM 06:00
#   7:00 AM 07:00
#   8:00 AM 08:00
#   9:00 AM 09:00
#   10:00 AM        10:00
#   11:00 AM        11:00
#   12:00 PM        12:00
#   1:00 PM 13:00
#   2:00 PM 14:00
#   3:00 PM 15:00
#   4:00 PM 16:00
#   5:00 PM 17:00
#   6:00 PM 18:00
#   7:00 PM 19:00
#   8:00 PM 20:00
#   9:00 PM 21:00
#   10:00 PM        22:00
#   11:00 PM        23:00
#   12:00 AM        00:00
#   In a file called working.py, implement a function called convert that expects a str in either of
#   the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to
#   17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will
#   be a space before each. Assume that these times are representative of actual times, not
#   necessarily 9:00 AM and 5:00 PM specifically.
#   
#   9:00 AM to 5:00 PM
#   9 AM to 5 PM
#   Raise a ValueError instead if the input to convert is not in either of those formats or if
#   either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours
#   will start ante meridiem and end post meridiem; someone might work late and even long hours
#   (e.g., 5:00 PM to 9:00 AM).
# ---- model response below: edit from here ----
def convert(time_str):
    """
    Converts a time string from 12-hour format to 24-hour format.

    Args:
        time_str (str): A string representing a time in 12-hour format, e.g., "9:00 AM to 5:00 PM".

    Returns:
        str: The time in 24-hour format, e.g., "09:00 to 17:00".

    Raises:
        ValueError: If the input time string is not in the correct format or if either time is invalid.
    """

    # Split the input string into start and end times
    start, end = time_str.split(' to ')

    # Split each time into hours and AM/PM
    start_hour, start_am_pm = start.split()
    end_hour, end_am_pm = end.split()

    # Check if the AM/PM is valid
    if start_am_pm not in ['AM', 'PM'] or end_am_pm not in ['AM', 'PM']:
        raise ValueError("Invalid AM/PM in time string")

    # Convert the hours to 24-hour format
    start_hour = int(start_hour)
    end_hour = int(end_hour)

    # Handle 12-hour to 24-hour conversion
    if start_am_pm == 'AM':
        if start_hour == 12:
            start_hour = 0
    else:
        if start_hour != 12:
            start_hour += 12

    if end_am_pm == 'AM':
        if end_hour == 12:
            end_hour = 0
    else:
        if end_hour != 12:
            end_hour += 12

    # Check if the hours are valid
    if start_hour < 0 or start_hour > 23 or end_hour < 0 or end_hour > 23:
        raise ValueError("Invalid hour in time string")

    # Format the hours as strings with leading zeros if necessary
    start_hour_str = f"{start_hour:02d}"
    end_hour_str = f"{end_hour:02d}"

    # Return the time in 24-hour format
    return f"{start_hour_str}:{start_hour_str.zfill(2)} to {end_hour_str}:{end_hour_str.zfill(2)}"


# Example usage:
print(convert("9:00 AM to 5:00 PM"))  # Output: 09:00 to 17:00
print(convert("9 AM to 5 PM"))  # Output: 09:00 to 17:00
print(convert("12:00 AM to 12:00 PM"))  # Output: 00:00 to 12:00
print(convert("12:00 PM to 12:00 AM"))  # Output: 12:00 to 00:00

# Test error handling
try:
    print(convert("9:00 AM to 25:00 PM"))  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Invalid hour in time string

try:
    print(convert("9:00 AM to 5:60 PM"))  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Invalid hour in time string

try:
    print(convert("9:00 AM to 5:00"))  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Invalid AM/PM in time string