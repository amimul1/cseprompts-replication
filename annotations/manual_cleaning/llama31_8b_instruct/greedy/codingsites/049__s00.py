# ================= CSEPrompts manual cleaning =================
# task: codingsites/049 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   You are given a 2-D array with dimensions N x M. Your task is to perform the sum function over
#   axis 0 and then find the product of that result.
# ---- model response below: edit from here ----
import numpy as np

# Define a 2-D array with dimensions N x M
N = 3
M = 4
arr = np.random.randint(0, 10, size=(N, M))  # Generate a random 2-D array

print("Original array:")
print(arr)

# Perform sum over axis 0
sum_over_axis_0 = np.sum(arr, axis=0)

print("\nSum over axis 0:")
print(sum_over_axis_0)

# Find the product of the result
product = np.prod(sum_over_axis_0)

print("\nProduct of the sum over axis 0:")
print(product)