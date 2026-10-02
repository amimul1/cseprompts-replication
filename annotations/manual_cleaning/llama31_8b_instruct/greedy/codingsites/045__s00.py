# ================= CSEPrompts manual cleaning =================
# task: codingsites/045 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   You are given two arrays A and B. Both have dimensions of N x N. Your task is to compute their
#   matrix product.
# ---- model response below: edit from here ----

import numpy as np

def matrix_multiply(A, B):
    """
    Compute the matrix product of two matrices A and B.

    Args:
        A (numpy.ndarray): The first matrix.
        B (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The matrix product of A and B.

    Raises:
        ValueError: If the number of columns in A does not match the number of rows in B.
    """
    # Check if the number of columns in A matches the number of rows in B
    if A.shape[1] != B.shape[0]:
        raise ValueError("The number of columns in A must match the number of rows in B")

    # Use numpy's matmul function to compute the matrix product
    return np.matmul(A, B)