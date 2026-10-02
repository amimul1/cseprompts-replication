# ================= CSEPrompts manual cleaning =================
# task: academic/007 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in
#   these denominations: 25 cents, 10 cents, and 5 cents.
#   
#   Implement a program that prompts the user to insert a coin, one at a time, each time informing
#   the user of the amount due. Once the user has inputted at least 50 cents, output how many cents
#   in change the user is owed. Assume that the user will only input integers, and ignore any
#   integer that isn’t an accepted denomination.
# ---- model response below: edit from here ----
def calculate_change():
    """
    Calculates the change owed to the user after inserting coins.
    """
    total_amount = 0  # Initialize total amount to 0
    due_amount = 50  # Amount due for a bottle of Coke

    while True:
        # Prompt user to insert a coin
        coin = input("Insert a coin (25, 10, or 5 cents): ")

        # Validate user input
        if coin not in ['25', '10', '5']:
            print("Invalid coin denomination. Please try again.")
            continue

        # Convert input to integer
        coin = int(coin)

        # Add coin to total amount
        total_amount += coin

        # Display current amount due
        due_amount = max(0, due_amount - coin)
        print(f"Amount due: ${due_amount} cents")

        # Check if user has paid enough
        if total_amount >= due_amount:
            # Calculate change
            change = total_amount - due_amount
            print(f"Thank you! Your change is ${change} cents.")
            break

calculate_change()