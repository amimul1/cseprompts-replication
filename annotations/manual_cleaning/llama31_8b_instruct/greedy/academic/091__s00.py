# ================= CSEPrompts manual cleaning =================
# task: academic/091 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Remember that Fibonacci's sequence is a sequence of numbers
#   #where every number is the sum of the previous two numbers.
#   #
#   #There exists a variant of Fibonacci's sequence called
#   #Fibonacci's multiplicative sequence. Fibonacci's
#   #multiplicative sequence is identical to Fibonacci's
#   #sequence, except that each number is the PRODUCT of the
#   #previous two numbers instead of the sum. Let's call these
#   #FibMult numbers.
#   #
#   #In order to make this interesting, we set the first two
#   #FibMult numbers to 1 and 2. So, the 1st FibMult number is
#   #1, and the second FibMult number is 2.
#   #
#   #So, here are the first few FibMult numbers:
#   #
#   #         n  = 1 2 3 4 5  6   7    8       9          10
#   # FibMult(n) = 1 2 2 4 8 32 256 8192 2097152 17179869184
#   #
#   #The sequence gets large fast!
#   #
#   #Write the function fib_mult using recursion. fib_mult
#   #takes as input an integer, and returns the FibMult
#   #number corresponding to that integer. For example:
#   #
#   # - fib_mult(1) = 1
#   # - fib_mult(2) = 2
#   # - fib_mult(3) = 2
#   # - fib_mult(9) = 2097152
#   # - fib_mult(12) = 618970019642690137449562112
#   #
#   #fib_mult MUST be implemented recursively.
#   #
#   #Hint: You will actually have two separate base cases,
#   #one for n = 1 and one for n = 2.
# ---- model response below: edit from here ----
### Fibonacci Multiplicative Sequence using Recursion
def fib_mult(n):
    """
    Calculate the nth Fibonacci multiplicative number.

    Args:
    n (int): The position of the number in the sequence.

    Returns:
    int: The nth Fibonacci multiplicative number.

    Raises:
    ValueError: If n is less than 1.
    """

    # Base case: If n is 1, return 1
    if n == 1:
        return 1
    
    # Base case: If n is 2, return 2
    elif n == 2:
        return 2
    
    # Recursive case: For n > 2, calculate the nth number as the product of the two preceding numbers
    else:
        return fib_mult(n-1) * fib_mult(n-2)