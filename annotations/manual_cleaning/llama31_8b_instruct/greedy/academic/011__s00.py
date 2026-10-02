# ================= CSEPrompts manual cleaning =================
# task: academic/011 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4
#   indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that
#   a tank is 75% full.
#   
#   implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X
#   and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much
#   fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank
#   is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is
#   essentially full.
#   
#   If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user
#   again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or
#   ZeroDivisionError.
# ---- model response below: edit from here ----
def get_percentage():
    """
    Continuously prompts the user for a fraction until a valid input is given.
    
    Returns:
        float: The percentage of fuel in the tank.
    """
    while True:
        try:
            # Get the fraction from the user
            fraction = input("Enter a fraction (X/Y): ")
            
            # Split the fraction into numerator and denominator
            numerator, denominator = map(int, fraction.split('/'))
            
            # Check if the denominator is zero
            if denominator == 0:
                print("Denominator cannot be zero. Please try again.")
                continue
            
            # Check if the numerator is greater than the denominator
            if numerator > denominator:
                print("Numerator cannot be greater than the denominator. Please try again.")
                continue
            
            # Calculate the percentage
            percentage = (numerator / denominator) * 100
            
            # Round the percentage to the nearest integer
            percentage = round(percentage)
            
            # Check if the percentage is 1% or less
            if percentage <= 1:
                return 'E'
            # Check if the percentage is 99% or more
            elif percentage >= 99:
                return 'F'
            else:
                return percentage
        
        except ValueError:
            print("Invalid input. Please enter a fraction in the format X/Y where X and Y are integers.")

def main():
    while True:
        percentage = get_percentage()
        if percentage == 'E':
            print("The tank is essentially empty.")
        elif percentage == 'F':
            print("The tank is essentially full.")
        else:
            print(f"The tank is {percentage}% full.")

if __name__ == "__main__":
    main()