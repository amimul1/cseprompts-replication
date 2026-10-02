# ================= CSEPrompts manual cleaning =================
# task: academic/099 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #The Greatest Common Factor (GCF) of two numbers is the
#   #largest number that divides evenly into those two
#   #numbers. For example, the Greatest Common Factor of 48
#   #and 18 is 6. 6 is the largest number that divides evenly
#   #into 48 (48 / 6 = 8) and 18 (18 / 6 = 3).
#   #
#   #Write a function called find_gcf. find_gcf should have
#   #two parameters, both integers. find_gcf should return
#   #the greatest common factor of those two numbers.
#   #
#   #For example:
#   #
#   # find_gcf(48, 18) -> 6
#   # find_gcf(21, 7) -> 7
#   # find_gcf(47, 17) -> 1
#   #
#   #If one number is a multiple of the other, the greatest
#   #common factor is the smaller number (e.g. 21 and 7). If
#   #the numbers have no common factors, then their greatest
#   #common factor is 1 (e.g. 47 and 17).
# ---- model response below: edit from here ----
def find_gcf(num1, num2):
    """
    Calculate the greatest common factor (GCF) of two integers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The greatest common factor of num1 and num2.
    """
    # Ensure num1 is the smaller number to simplify the calculation
    if num2 > num1:
        num1, num2 = num2, num1

    # Use a while loop to find the GCF
    while num2 != 0:
        # Calculate the remainder of num1 divided by num2
        remainder = num1 % num2
        # Update num1 to be the previous num2 and num2 to be the remainder
        num1, num2 = num2, remainder

    # At this point, num1 is the GCF
    return num1