# ================= CSEPrompts manual cleaning =================
# task: codingsites/046 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   You are given two arrays: A and B. Your task is to compute their inner and outer product.
# ---- model response below: edit from here ----
import numpy as np

# Define two arrays
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Inner Product (Dot Product)
inner_product = np.dot(A, B)
print("Inner Product (Dot Product):", inner_product)

# Outer Product
outer_product = np.outer(A, B)
print("Outer Product:")
print(outer_product)