# ================= CSEPrompts manual cleaning =================
# task: academic/038 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   balance = 500
#   income = 200
#   price = 1000
#   months = 6
#   
#   #You may modify the lines of code above, but don't move them!
#   #When you Submit your code, we'll change these lines to
#   #assign different values to the variables.
#   
#   #You're thinking of buying a new computer. The variables
#   #above represent the balance of your bank account, your
#   #monthly disposable income, the total price of the computer,
#   #and the number of months that the retailer will give you to
#   #pay off the computer.
#   #
#   #You can buy the computer if either (a) you can afford to
#   #buy the computer in cash right now (balance is greater than
#   #price), or (b) you can afford the monthly payments (income
#   #is greater than price divided by months).
#   #
#   #In other words, if a computer cost $1200 and you spread it
#   #out over 12 months, you would need your monthly available
#   #income to be at least $100 to buy the computer, or you
#   #would need your current bank balance to be at least $1200.
#   #
#   #Add some code below that will print True if you're able to
#   #afford the computer given the values above, and False if you
#   #are not.
#   
#   
#   #Add your code below!
# ---- model response below: edit from here ----
balance = 500
income = 200
price = 1000
months = 6

# Check if you can afford the computer in cash
can_afford_cash = balance >= price

# Check if you can afford the monthly payments
can_afford_monthly = income >= (price / months)

# You can buy the computer if you can afford it in cash or with monthly payments
can_afford = can_afford_cash or can_afford_monthly

print(can_afford)