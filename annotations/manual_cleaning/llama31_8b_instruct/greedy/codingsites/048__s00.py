# ================= CSEPrompts manual cleaning =================
# task: codingsites/048 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   You are given a 2-D array with dimensions N x M. Your task is to perform the min function over
#   axis 1 and then find the max of that.
# ---- model response below: edit from here ----
import numpy as np

# Define a 2D array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Perform min function over axis 1
min_over_axis1 = np.min(arr, axis=1)

# Find the max of the result
max_of_min = np.max(min_over_axis1)

print("Original array:")
print(arr)
print("\nMin over axis 1:")
print(min_over_axis1)
print("\nMax of min over axis 1:")
print(max_of_min)