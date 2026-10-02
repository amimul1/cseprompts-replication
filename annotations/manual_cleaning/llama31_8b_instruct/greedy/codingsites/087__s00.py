# ================= CSEPrompts manual cleaning =================
# task: codingsites/087 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   The NumPy module also comes with a number of built-in routines for linear algebra calculations.
#   These can be found in the sub-module linalg. linalg.det The linalg.det tool computes the
#   determinant of an array.
# ---- model response below: edit from here ----
import numpy as np

# Define a 2x2 matrix
matrix = np.array([[1, 2], [3, 4]])

# Compute the determinant of the matrix
determinant = np.linalg.det(matrix)

print("Determinant of the matrix: ", determinant)