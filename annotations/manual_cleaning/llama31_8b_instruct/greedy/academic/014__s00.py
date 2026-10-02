# ================= CSEPrompts manual cleaning =================
# task: academic/014 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY),
#   otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t
#   be easily sorted because the date’s year comes last instead of first. Try sorting, for instance,
#   2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in
#   that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could
#   also be interpreted as August 9, 1636!
#   
#   Fortunately, computers tend to use ISO 8601, an international standard that prescribes that
#   dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country,
#   formatting years with four digits, months with two digits, and days with two digits, “padding”
#   each with leading zeroes as needed.
#   
#   In a file called outdated.py, implement a program that prompts the user for a date, anno Domini,
#   in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the
#   latter might be any of the values in the list below:
#   
#   [
#       "January",
#       "February",
#       "March",
#       "April",
#       "May",
#       "June",
#       "July",
#       "August",
#       "September",
#       "October",
#       "November",
#       "December"
#   ]
#   Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in
#   either format, prompt the user again. Assume that every month has no more than 31 days; no need
#   to validate whether a month has 28, 29, 30, or 31 days.
# ---- model response below: edit from here ----
# outdated.py

import re
from datetime import datetime

# List of month names
MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def get_date_from_user():
    """Prompt the user for a date and return it in YYYY-MM-DD format."""
    while True:
        user_input = input("Enter a date (MM/DD/YYYY or month day, year): ")
        
        # Try to parse the date in month-day-year format
        match = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", user_input)
        if match:
            month, day, year = map(int, match.groups())
            if 1 <= month <= 12 and 1 <= day <= 31:
                return f"{year:04d}-{month:02d}-{day:02d}"
        
        # Try to parse the date in month day, year format
        for month_name in MONTHS:
            if month_name in user_input:
                month_index = MONTHS.index(month_name)
                match = re.search(rf"{month_name}\s+(\d{1,2}),\s+(\d{4})", user_input)
                if match:
                    day, year = map(int, match.groups())
                    if 1 <= day <= 31:
                        return f"{year:04d}-{month_index+1:02d}-{day:02d}"
        
        print("Invalid date. Please try again.")

def main():
    print("Enter a date in MM/DD/YYYY or month day, year format.")
    print("For example: 9/8/1636 or September 8, 1636")
    print()
    
    while True:
        date = get_date_from_user()
        print(f"Date in YYYY-MM-DD format: {date}")
        cont = input("Do you want to enter another date? (yes/no): ")
        if cont.lower() != "yes":
            break

if __name__ == "__main__":
    main()