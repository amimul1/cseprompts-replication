# ================= CSEPrompts manual cleaning =================
# task: academic/023 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   implement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:
#   
#   convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns
#   that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X
#   and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
#   If Y is 0, then convert should raise a ZeroDivisionError.
#   gauge expects an int and returns a str that is:
#   "E" if that int is less than or equal to 1,
#   "F" if that int is greater than or equal to 99,
#   and "Z%" otherwise, wherein Z is that same int.
#   
#   here is the Fuel Gauge from Problem Set 3:
#   
#   Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4
#   indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that
#   a tank is 75% full.
#   
#   In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as
#   X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the
#   nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead
#   to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to
#   indicate that the tank is essentially full.
#   
#   If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user
#   again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or
#   ZeroDivisionError.
# ---- model response below: edit from here ----
def convert(fraction):
    """
    Converts a fraction in X/Y format to a percentage rounded to the nearest int between 0 and 100, inclusive.

    Args:
        fraction (str): A string representing a fraction in X/Y format.

    Returns:
        int: The percentage of the fraction.

    Raises:
        ValueError: If X or Y is not an integer, or if X is greater than Y.
        ZeroDivisionError: If Y is 0.
    """
    try:
        numerator, denominator = map(int, fraction.split('/'))
        if numerator > denominator:
            raise ValueError("Numerator cannot be greater than denominator")
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be 0")
        return round((numerator / denominator) * 100)
    except ValueError as e:
        raise ValueError(str(e))
    except ZeroDivisionError as e:
        raise ZeroDivisionError(str(e))


def gauge(fuel_level):
    """
    Returns a string indicating the fuel level as E, F, or a percentage.

    Args:
        fuel_level (int): The fuel level as a percentage.

    Returns:
        str: A string indicating the fuel level.
    """
    if fuel_level <= 1:
        return "E"
    elif fuel_level >= 99:
        return "F"
    else:
        return f"{fuel_level}%"


def main():
    while True:
        try:
            fraction = input("Enter a fraction (X/Y): ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError) as e:
            print(f"Invalid input: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()