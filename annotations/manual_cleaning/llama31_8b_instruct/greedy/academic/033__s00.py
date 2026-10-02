# ================= CSEPrompts manual cleaning =================
# task: academic/033 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#   Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked
#   above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be
#   498.75). You should use input to read a string and float() to convert the string to a number. Do
#   not worry about error checking the user input - assume the user types numbers properly.
# ---- model response below: edit from here ----
def calculate_gross_pay(hours, rate):
    """
    Calculate the gross pay based on the hours worked and the hourly rate.

    :param hours: The number of hours worked
    :param rate: The hourly rate
    :return: The gross pay
    """
    if hours <= 40:
        return hours * rate
    else:
        return 40 * rate + (hours - 40) * rate * 1.5

def main():
    # Prompt the user for hours and rate
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate: "))

    # Calculate the gross pay
    gross_pay = calculate_gross_pay(hours, rate)

    # Print the result
    print(f"Gross Pay: ${gross_pay:.2f}")

if __name__ == "__main__":
    main()