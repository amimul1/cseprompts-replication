# ================= CSEPrompts manual cleaning =================
# task: academic/049 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #A common formula in probability and statistics is the
#   #formula for the number of possible combinations of r
#   #objects from a set of n objects. For example, the question,
#   #"How many possible 2-card hands can you deal from a deck of
#   #52 unique cards?" is saying, "How many combinations of 2
#   #can you make from a set of 52?"
#   #
#   #The formula for the number of combinations of length r from
#   #a set of n objects is:
#   #
#   #  numCombinations = n! / r!(n-r)!
#   #
#   #The ! mark is the symbol for factorial. Factorial means the
#   #product of the number times every number between itself and
#   #1. For example, 5! is 120: 5 * 4 * 3 * 2 * 1 = 120.
#   #
#   #Write a function called numCombinations with two parameters:
#   #n, the number of objects from which to choose, and r, the
#   #number of objects to choose. numCombinations should return
#   #the number of combinations according to the formula above.
#   #Don't worry if you don't fully understand what combinations
#   #are -- just focus on implementing a function that solves
#   #that formula given n and r.
#   #
#   #You may *not* use Python's built-in factorial method to
#   #complete this; you should implement that yourself.
#   #
#   #Hint: We'd suggest writing two functions: factorial() and
#   #numCombinations(). Then, call factorial() in your code for
#   #numCombinations(). You don't have to do this, but it will
#   #make your answer a little easier!
#   #
#   #Hint 2: Remember to put parentheses around the denominator.
# ---- model response below: edit from here ----
def factorial(n):
    """
    Calculate the factorial of a given number n.
    
    Args:
        n (int): The number to calculate the factorial of.
    
    Returns:
        int: The factorial of n.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def numCombinations(n, r):
    """
    Calculate the number of combinations of r objects from a set of n objects.
    
    Args:
        n (int): The total number of objects.
        r (int): The number of objects to choose.
    
    Returns:
        int: The number of combinations of r objects from a set of n objects.
    """
    return factorial(n) // factorial(r) // factorial(n - r)

# Example usage:
n = 52  # Total number of cards in a deck
r = 2   # Number of cards to choose
print(f"The number of possible {r}-card hands from a deck of {n} unique cards is: {numCombinations(n, r)}")