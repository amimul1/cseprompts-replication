# ================= CSEPrompts manual cleaning =================
# task: codingsites/047 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   You are given a 2-D array of size N x M. Your task is to find: The mean along axis 1. The var
#   along axis 0. The std along axis None.
# ---- model response below: edit from here ----
import numpy as np

# Define a 2D array
N = 3
M = 4
arr = np.random.randint(1, 100, size=(N, M))

print("Original array:")
print(arr)

# Calculate mean along axis 1
mean_along_axis_1 = np.mean(arr, axis=1)
print("\nMean along axis 1:")
print(mean_along_axis_1)

# Calculate variance along axis 0
var_along_axis_0 = np.var(arr, axis=0)
print("\nVariance along axis 0:")
print(var_along_axis_0)

# Calculate standard deviation along axis None (flattened array)
std_along_none = np.std(arr.flatten())
print("\nStandard deviation along axis None (flattened array):")
print(std_along_none)