# ================= CSEPrompts manual cleaning =================
# task: codingsites/086 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given the coefficients of the polynomial P, and the value for x, find the value of P when x = k.
# ---- model response below: edit from here ----
import numpy as np

def evaluate_polynomial(coefficients, x):
    """
    Evaluate a polynomial at a given value of x.

    Parameters:
    coefficients (list): Coefficients of the polynomial in descending order of powers.
    x (float): Value at which to evaluate the polynomial.

    Returns:
    float: Value of the polynomial at x.
    """
    return np.polyval(coefficients, x)