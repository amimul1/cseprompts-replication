# ================= CSEPrompts manual cleaning =================
# task: codingsites/044 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   You are given a square matrix A with dimensions N x N. Your task is to find the determinant.
# ---- model response below: edit from here ----
import numpy as np

def calculate_determinant(matrix):
    """
    Calculate the determinant of a square matrix.

    Args:
        matrix (list of lists): A 2D list representing the square matrix.

    Returns:
        float: The determinant of the matrix.
    """
    # Convert the input list to a numpy array
    matrix = np.array(matrix)

    # Check if the input matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square")

    # Calculate the determinant using the numpy linalg.det function
    determinant = np.linalg.det(matrix)

    return determinant