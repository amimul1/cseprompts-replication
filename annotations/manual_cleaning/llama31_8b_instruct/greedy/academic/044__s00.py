# ================= CSEPrompts manual cleaning =================
# task: academic/044 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   amount = 17
#   
#   #You may modify the lines of code above, but don't move them!
#   #When you Submit your code, we'll change these lines to
#   #assign different values to the variables.
#   #
#   #The variable above describes an amount of money measured in
#   #dollars. Imagine you want to select the bills (1-dollar bills,
#   #5-dollar bills, 10-dollar bills, etc.) that make up that
#   #amount of money. For example, 17 dollars is one $10, one $5,
#   #and two $1s.
#   #
#   #Write a program that will print out the bills needed to
#   #arrive at the amount shown above. Assume that we always want
#   #the maximum number of large bills: for example, for 17 dollars,
#   #we want one $10, one $5, and two $1s, not three $5s and two $1s.
#   #You may assume that the largest bill you have on hand is a
#   #$50-dollar bill.
#   #
#   #Your code should print the following (with the correct numbers
#   #based on the value of amount):
#   #
#   #Fifties: 0
#   #Twenties: 0
#   #Tens: 1
#   #Fives: 1
#   #Ones: 2
# ---- model response below: edit from here ----
def calculate_bills(amount):
    """
    Calculate the number of bills needed to make up a given amount of money.

    Args:
        amount (int): The amount of money in dollars.

    Returns:
        None
    """
    # Define the denominations of the bills
    denominations = [50, 20, 10, 5, 1]

    # Print the header
    print("Bills needed to make up ${}:".format(amount))

    # Iterate over the denominations in descending order
    for denomination in denominations:
        # Calculate the number of bills of the current denomination
        num_bills = amount // denomination
        # Update the remaining amount
        amount %= denomination
        # Print the number of bills
        print("{}s: {}".format(denomination, num_bills))

# Test the function
amount = 17
calculate_bills(amount)
