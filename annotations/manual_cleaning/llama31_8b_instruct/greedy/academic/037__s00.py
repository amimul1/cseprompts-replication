# ================= CSEPrompts manual cleaning =================
# task: academic/037 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   old_balance = "500.45"
#   deposit = "10"
#   
#   #You may modify the lines of code above, but don't move them!
#   #When you Submit your code, we'll change these lines to
#   #assign different values to the variables.
#   
#   #Imagine you're writing code for an ATM that accepts cash
#   #deposits. You need to update the customer's balance based
#   #on a deposit amount. However, both the old balance and the
#   #deposit are given as strings.
#   #
#   #Write code below that will print the new balance after the
#   #deposit is processed. This should be printed along with
#   #the following text labeling the amount:
#   #
#   #The new balance is: 510.45
#   #
#   #Note that the old balance will always include change, but
#   #the deposit will never include change because the ATM has
#   #no coin slot, only a slot for paper money.
#   #
#   #With the initial values of the variables shown above, your
#   #code should print the text shown on line 17.
#   
#   
#   #Add your code here!
# ---- model response below: edit from here ----
old_balance = "500.45"
deposit = "10"

# Convert the old balance and deposit from strings to floats
old_balance = float(old_balance)
deposit = float(deposit)

# Calculate the new balance by adding the deposit to the old balance
new_balance = old_balance + deposit

# Print the new balance with the specified label
print(f"The new balance is: {new_balance:.2f}")