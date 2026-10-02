# ================= CSEPrompts manual cleaning =================
# task: codingsites/117 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Use subsetting to find out which observations in our BMI array are above 23
# ---- model response below: edit from here ----
### Subsetting to Find Observations Above a Certain Value


# Create a sample DataFrame with BMI data
data = {
    'Name': ['John', 'Mary', 'David', 'Emily', 'Michael'],
    'Age': [25, 31, 42, 28, 35],
    'BMI': [20, 22, 25, 18, 30]
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Subset the DataFrame to find observations with BMI above 23
above_23_bmi = df[df['BMI'] > 23]

# Print the subsetted DataFrame
print("\nObservations with BMI above 23:")
print(above_23_bmi)
