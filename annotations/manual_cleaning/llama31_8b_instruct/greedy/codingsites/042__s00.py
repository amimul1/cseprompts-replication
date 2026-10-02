# ================= CSEPrompts manual cleaning =================
# task: codingsites/042 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   You are given a function f(X) = X^2. You are also given K lists. The ith list consists of Ni
#   elements. You have to pick one element from each list so that the value from the equation below
#   is maximized: S = (f(X1) + f(X2) + ... + f(Xk)) % M. Xi denotes the element picked from the ith
#   list. Compute the maximum value of S % M.
# ---- model response below: edit from here ----
### Problem: Maximizing the Sum of Squares Modulo M

### Solution

def max_sum_of_squares(lists, M):
    """
    This function calculates the maximum value of S = (f(X1) + f(X2) + ... + f(Xk)) % M.
    
    Args:
    lists (list of lists): A list of K lists, each containing Ni elements.
    M (int): The modulo value.
    
    Returns:
    int: The maximum value of S % M.
    """
    
    # Initialize the maximum sum
    max_sum = 0
    
    # Iterate over each list
    for lst in lists:
        # Find the maximum element in the list
        max_element = max(lst)
        
        # Add the square of the maximum element to the sum
        max_sum += max_element ** 2
        
        # Take the modulo M to prevent overflow
        max_sum %= M
    
    # Return the maximum sum
    return max_sum

# Example usage:
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M = 1000
print(max_sum_of_squares(lists, M))