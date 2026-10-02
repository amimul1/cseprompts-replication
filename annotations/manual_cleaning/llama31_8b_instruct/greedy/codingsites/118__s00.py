# ================= CSEPrompts manual cleaning =================
# task: codingsites/118 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Convert the list of weights from a list to a Numpy array. Then, convert all of the weights from
#   kilograms to pounds. Use the scalar conversion of 2.2 lbs per kilogram to make your conversion.
#   Lastly, print the resulting array of weights in pounds
# ---- model response below: edit from here ----
import numpy as np

# Define the list of weights in kilograms
weights_kg = [50, 60, 70, 80, 90]

# Convert the list to a Numpy array
weights_array = np.array(weights_kg)

# Convert the weights from kilograms to pounds using the scalar conversion
weights_lbs = weights_array * 2.2

# Print the resulting array of weights in pounds
print(weights_lbs)
