# ================= CSEPrompts manual cleaning =================
# task: academic/002 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   implement a program that prompts the user for a greeting. If the greeting starts with “hello”,
#   output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output
#   $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-
#   insensitively.
# ---- model response below: edit from here ----
def calculate_price(greeting):
    """
    Calculate the price based on the greeting.

    Args:
        greeting (str): The user's greeting.

    Returns:
        int: The calculated price.
    """
    greeting = greeting.strip().lower()  # Remove leading whitespace and convert to lowercase
    if greeting.startswith('hello'):
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100

def main():
    # Prompt the user for a greeting
    greeting = input("Please enter a greeting: ")
    
    # Calculate and print the price
    price = calculate_price(greeting)
    print(f"The price is: ${price}")

if __name__ == "__main__":
    main()
