# ================= CSEPrompts manual cleaning =================
# task: codingsites/115 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create two Python lists for height and weight. Then, import the numpy package and create numpy
#   arrays out of the newly created lists
# ---- model response below: edit from here ----

# Import the numpy package
import numpy as np

# Create two lists for height and weight
height = [175, 165, 180, 168, 182, 170, 178, 172, 185, 177]
weight = [65, 60, 75, 70, 80, 72, 78, 68, 85, 75]

# Print the lists before conversion
print("Height (List):", height)
print("Weight (List):", weight)

# Convert the lists to numpy arrays
height_array = np.array(height)
weight_array = np.array(weight)

# Print the numpy arrays
print("\nHeight (Numpy Array):", height_array)
print("Weight (Numpy Array):", weight_array)

# Print the data types of the numpy arrays
print("\nData Type of Height Array:", height_array.dtype)
print("Data Type of Weight Array:", weight_array.dtype)
