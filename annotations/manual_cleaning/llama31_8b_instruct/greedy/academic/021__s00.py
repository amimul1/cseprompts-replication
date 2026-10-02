# ================= CSEPrompts manual cleaning =================
# task: academic/021 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   implement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below,
#   wherein value expects a str as input and returns 0 if that str starts with “hello”, 20 if that
#   str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively.
#   You can assume that the string passed to the value function will not contain any leading spaces.
#   Only main should call print.
#   
#   here is the Home Federal Savings Bank from Problem Set 1:
#   In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone
#   who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t
#   a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a
#   greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.
#   
#   implement a program that prompts the user for a greeting. If the greeting starts with “hello”,
#   output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output
#   $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-
#   insensitively.
# ---- model response below: edit from here ----
def value(greeting: str) -> int:
    """
    Returns the amount of money based on the greeting.
    
    Args:
    greeting (str): The greeting to check.
    
    Returns:
    int: The amount of money.
    """
    # Remove leading whitespace and convert to lowercase for case-insensitive comparison
    greeting = greeting.lstrip().lower()
    
    # Check if the greeting starts with "hello"
    if greeting.startswith("hello"):
        return 0
    # Check if the greeting starts with "h" but not "hello"
    elif greeting.startswith("h"):
        return 20
    # If the greeting does not start with "h", return 100
    else:
        return 100


def main():
    # Prompt the user for a greeting
    greeting = input("Please enter a greeting: ")
    
    # Get the amount of money based on the greeting
    amount = value(greeting)
    
    # Print the result
    print(f"You are owed ${amount}.")


if __name__ == "__main__":
    main()