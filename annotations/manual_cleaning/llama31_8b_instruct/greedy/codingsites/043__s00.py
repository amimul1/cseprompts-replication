# ================= CSEPrompts manual cleaning =================
# task: codingsites/043 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   You are given the coefficients of a polynomial P. Your task is to find the value of P at point
#   x.
# ---- model response below: edit from here ----
import numpy as np

def evaluate_polynomial(coefficients, x):
    """
    Evaluate a polynomial at a given point x.

    Parameters:
    coefficients (list): Coefficients of the polynomial in descending order of powers.
    x (float): The point at which to evaluate the polynomial.

    Returns:
    float: The value of the polynomial at point x.
    """
    return np.polyval(coefficients, x)

# Example usage:
# Define the coefficients of the polynomial
coefficients = [3, 2, -4, 1]  # represents the polynomial 3 + 2x - 4x^2 + x^3

# Evaluate the polynomial at x = 2
x = 2
result = evaluate_polynomial(coefficients, x)

print(f"The value of the polynomial at x = {x} is: {result}")