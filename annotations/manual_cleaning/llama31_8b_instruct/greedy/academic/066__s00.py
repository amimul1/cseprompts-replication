# ================= CSEPrompts manual cleaning =================
# task: academic/066 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called is_prime. is_prime should take
#   #as input one integer. It should return True if the integer
#   #is prime, False if the integer is not prime. You may
#   #assume the integer will be greater than 2 and less than
#   #1000.
#   #
#   #Remember, a prime number is one into which no number is
#   #divisible besides 1 and itself. For example, 6 is not
#   #prime because it is divisible by 2 and 3. 7 is prime
#   #because it is only divisible by 1 and itself.
#   #
#   #HINT: Remember, once you find a _single_ factor of the
#   #number, you can return False: it only takes one factor
#   #to make the number not prime.
# ---- model response below: edit from here ----
## is_prime Function
### Checks if a given integer is prime
def is_prime(n):
    """
    Checks if a given integer is prime.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    # Prime numbers are greater than 1
    if n <= 1:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # All other even numbers are not prime
    if n % 2 == 0:
        return False

    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    # If no factors are found, the number is prime
    return True