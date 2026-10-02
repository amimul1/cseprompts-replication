# ================= CSEPrompts manual cleaning =================
# task: academic/018 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that
#   would generate ten different math problems for David to solve. For instance, if the toy were to
#   display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = ,
#   David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would
#   display EEE. And after three incorrect answers for the same problem, the toy would simply
#   display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).
#   
#   In a file called professor.py, implement a program that:
#   
#   Prompts the user for a level,
#   . If the user does not input 1, 2, or 3, the program should prompt again.
#   Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a
#   non-negative integer with
#    digits. No need to support operations other than addition (+).
#   Prompts the user to solve each of those problems. If an answer is not correct (or not even a
#   number), the program should output EEE and prompt the user again, allowing the user up to three
#   tries in total for that problem. If the user has still not answered correctly after three tries,
#   the program should output the correct answer.
#   The program should ultimately output the user’s score: the number of correct answers out of 10.
#   Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the
#   user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-
#   negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
#   
#   import random
#   
#   
#   def main():
#       ...
#   
#   
#   def get_level():
#       ...
#   
#   
#   def generate_integer(level):
#       ...
#   
#   
#   if __name__ == "__main__":
#       main()
# ---- model response below: edit from here ----
import random

def get_level():
    """
    Prompts the user for a level and returns 1, 2, or 3.
    If the user does not input 1, 2, or 3, the function prompts again.
    """
    while True:
        try:
            level = int(input("Enter a level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_integer(level):
    """
    Randomly generates a non-negative integer with level digits.
    Raises a ValueError if level is not 1, 2, or 3.
    """
    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, or 3")
    max_value = 10 ** level - 1
    return random.randint(0, max_value)

def main():
    """
    Prompts the user for a level, generates 10 math problems, and calculates the user's score.
    """
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = f"{x} + {y} = "
        for attempt in range(3):
            try:
                answer = int(input(problem))
                if answer == x + y:
                    score += 1
                    print("Correct!")
                    break
                else:
                    print("EEE")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print(f"Correct answer: {x + y}")
    print(f"Your score: {score} out of 10")

if __name__ == "__main__":
    main()