# ================= CSEPrompts manual cleaning =================
# task: academic/017 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   I’m thinking of a number between 1 and 100…
#   
#   What is it?
#   In a file called game.py, implement a program that:
#   
#   Prompts the user for a level,
#   . If the user does not input a positive integer, the program should prompt again.
#   Randomly generates an integer between 1 and
#   , inclusive, using the random module.
#   Prompts the user to guess that integer. If the guess is not a positive integer, the program
#   should prompt the user again.
#   If the guess is smaller than that integer, the program should output Too small! and prompt the
#   user again.
#   If the guess is larger than that integer, the program should output Too large! and prompt the
#   user again.
#   If the guess is the same as that integer, the program should output Just right! and exit.
# ---- model response below: edit from here ----
import random

def get_level():
    """Prompts the user for a level and ensures it's a positive integer."""
    while True:
        try:
            level = int(input("Enter a level (1-100): "))
            if 1 <= level <= 100:
                return level
            else:
                print("Please enter a level between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def get_user_guess(level):
    """Prompts the user for a guess and ensures it's a positive integer."""
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {level}: "))
            if guess > 0:
                return guess
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def play_game():
    """Plays the number guessing game."""
    level = get_level()
    target = random.randint(1, level)
    while True:
        guess = get_user_guess(level)
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    play_game()