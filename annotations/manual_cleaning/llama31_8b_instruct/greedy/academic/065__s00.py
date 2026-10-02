# ================= CSEPrompts manual cleaning =================
# task: academic/065 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #The Collatz Conjecture is a famous sequence in mathematics
#   #proposed by Lothar Collatz. It proceeds as follows:
#   #
#   #Start with any number. If the number is even, divide it by
#   #2. If the number is odd, triple it and add one. Repeat.
#   #Eventually, no matter what number you begin with, this
#   #sequence will converge on 1 (and if you continue repeating
#   #it, you'll repeat 1-4-2 infinitely).
#   #
#   #For example, imagine we started with the number 21:
#   #5 is odd, so 5 * 3 + 1 = 16
#   #16 is even, so 16 / 2 = 8
#   #8 is even, so 8 / 2 = 4
#   #4 is even, so 4 / 2 = 2
#   #2 is even, so 2 / 1 = 1
#   #
#   #Starting with 5, this sequence converges on 1 in 5
#   #iterations: 5 to 16, 16 to 8, 8 to 4, 4 to 2, and 2 to 1.
#   #
#   #Implement a function called collatz. collatz should take
#   #as input an integer, and return the number of iterations
#   #it takes for the Collatz sequence to reach 1 from that
#   #number. For example, collatz(5) would return 5 because
#   #it took 5 iterations to converge on 1.
# ---- model response below: edit from here ----
### Collatz Conjecture Implementation in Python
def collatz(n):
    """
    Calculate the number of iterations it takes for the Collatz sequence to reach 1 from a given number.

    Args:
        n (int): The starting number for the Collatz sequence.

    Returns:
        int: The number of iterations it takes for the Collatz sequence to reach 1.

    Raises:
        ValueError: If the input number is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")

    iterations = 0
    while n != 1:
        if n % 2 == 0:
            # If n is even, divide it by 2
            n = n // 2
        else:
            # If n is odd, triple it and add 1
            n = 3 * n + 1
        iterations += 1

    return iterations