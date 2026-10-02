# ================= CSEPrompts manual cleaning =================
# task: codingsites/116 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Perform element-wise calculations on height and weight. For example, you could take all 6 of the
#   height and weight observations above, and calculate the BMI for each observation with a single
#   equation
# ---- model response below: edit from here ----
# Define the heights and weights
heights = [1.68, 1.75, 1.65, 1.70, 1.60, 1.72]
weights = [65, 70, 60, 75, 55, 68]

# Calculate BMI for each observation
bmi = [weight / (height ** 2) for height, weight in zip(heights, weights)]

# Print the results
for i in range(len(heights)):
    print(f"Height: {heights[i]}m, Weight: {weights[i]}kg, BMI: {bmi[i]}")
