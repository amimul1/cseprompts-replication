# ================= CSEPrompts manual cleaning =================
# task: academic/098 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Remember that Fibonacci's sequence is a sequence of numbers
#   #where every number is the sum of the previous two numbers.
#   #
#   #Let's write a variant of Fibonacci's sequence called fib_skip.
#   #Here, every number will be the sum of the previous number,
#   #and the number two steps earlier. So, the fourth number is
#   #the sum of the third and first number; the fifth number is
#   #the sum of the second and fourth number; and so on.
#   #
#   #To do this, we must define the first three numbers of the
#   #sequence as 1, 1, 1. From there, the sequence continues:
#   #
#   # 1, 1, 1, 2, 3, 4, 6, 9, 13, 19, 28...
#   #
#   #For example, the last number is 28 because it is the sum
#   #of the previous number (19) and the number two steps before
#   #the previous number (9). So, fib_skip(11) = fib_skip(10) +
#   #fib_skip(8).
#   #
#   #Write the function fib_skip using recursion. fib_skip
#   #takes as input an integer, and returns the fib_skip
#   #number corresponding to that integer. For example:
#   #
#   # - fib_skip(1) = 1
#   # - fib_skip(2) = 1
#   # - fib_skip(3) = 1
#   # - fib_skip(4) = 3
#   # - fib_skip(9) = 13
#   # - fib_skip(11) = 28
#   #
#   #fib_skip MUST be implemented recursively.
#   #
#   #Hint: Think first about how many base cases you have!
#   #The base cases are the numbers for which the answer
#   #to fib_skip is _defined_, not _calculated_.
# ---- model response below: edit from here ----
def fib_skip(n):
    """
    Returns the nth number in the fib_skip sequence.

    The fib_skip sequence is a variant of Fibonacci's sequence where every number
    is the sum of the previous number and the number two steps earlier.

    Args:
        n (int): The position of the number in the sequence.

    Returns:
        int: The nth number in the fib_skip sequence.
    """

    # Base cases: fib_skip(1), fib_skip(2), and fib_skip(3) are all 1
    if n <= 3:
        return 1

    # Recursive case: fib_skip(n) = fib_skip(n-1) + fib_skip(n-3)
    else:
        return fib_skip(n-1) + fib_skip(n-3)