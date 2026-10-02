# ================= CSEPrompts manual cleaning =================
# task: codingsites/013 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Read two integers from STDIN and print three lines where: The first line contains the sum of the
#   two numbers. The second line contains the difference of the two numbers (first - second). The
#   third line contains the product of the two numbers.
# ---- model response below: edit from here ----
# Read two integers from STDIN
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the sum, difference, and product
sum_of_numbers = num1 + num2
difference = num1 - num2
product = num1 * num2

# Print the results
print("Sum:", sum_of_numbers)
print("Difference:", difference)
print("Product:", product)