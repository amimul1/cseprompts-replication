# ================= CSEPrompts manual cleaning =================
# task: academic/035 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#   Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all
#   hours worked above 40 hours. Put the logic to do the computation of pay in a function called
#   computepay() and use the function to do the computation. The function should return a value. Use
#   45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should
#   use input to read a string and float() to convert the string to a number. Do not worry about
#   error checking the user input unless you want to - you can assume the user types numbers
#   properly. Do not name your variable sum or use the sum() function.
# ---- model response below: edit from here ----
def computepay(hours, rate):
    """
    Compute the gross pay for a given number of hours and hourly rate.

    The pay is calculated as follows:
    - For hours up to 40, the pay is the hourly rate times the number of hours.
    - For hours above 40, the pay is the hourly rate times 40 plus one and a half times the hourly rate times the number of hours above 40.

    Args:
        hours (float): The number of hours worked.
        rate (float): The hourly rate.

    Returns:
        float: The gross pay.
    """
    if hours <= 40:
        return hours * rate
    else:
        return 40 * rate + (hours - 40) * 1.5 * rate


def main():
    # Get the number of hours from the user
    hours = float(input("Enter the number of hours worked: "))

    # Get the hourly rate from the user
    rate = float(input("Enter the hourly rate: "))

    # Compute the gross pay
    pay = computepay(hours, rate)

    # Print the gross pay
    print(f"The gross pay is: ${pay:.2f}")


if __name__ == "__main__":
    # Test the function with 45 hours and a rate of 10.50 per hour
    print("Testing the function with 45 hours and a rate of 10.50 per hour:")
    print(f"Expected pay: $498.75")
    print(f"Actual pay: {computepay(45, 10.50):.2f}")
    print()

    # Run the main program
    main()