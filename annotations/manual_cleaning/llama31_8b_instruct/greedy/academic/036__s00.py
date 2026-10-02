# ================= CSEPrompts manual cleaning =================
# task: academic/036 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#   Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters
#   anything other than a valid number catch it with a try/except and put out an appropriate message
#   and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
# ---- model response below: edit from here ----
def get_numbers():
    """Get numbers from the user until 'done' is entered."""
    numbers = []
    while True:
        user_input = input("Enter a number or 'done' to finish: ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
    return numbers

def print_results(numbers):
    """Print the largest and smallest numbers."""
    if not numbers:
        print("No numbers entered.")
    else:
        print(f"Largest number: {max(numbers)}")
        print(f"Smallest number: {min(numbers)}")

def main():
    numbers = get_numbers()
    print_results(numbers)

if __name__ == "__main__":
    main()