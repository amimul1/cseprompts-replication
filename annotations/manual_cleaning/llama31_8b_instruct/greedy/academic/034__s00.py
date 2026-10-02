# ================= CSEPrompts manual cleaning =================
# task: academic/034 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print
#   an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#   Score Grade
#   >= 0.9 A
#   >= 0.8 B
#   >= 0.7 C
#   >= 0.6 D
#   < 0.6 F
#   If the user enters a value out of range, print a suitable error message and exit. For the test,
#   enter a score of 0.85.
# ---- model response below: edit from here ----
def get_grade(score):
    """
    Returns the grade based on the given score.

    Args:
        score (float): The score between 0.0 and 1.0.

    Returns:
        str: The corresponding grade.
    """
    if score < 0.0 or score > 1.0:
        raise ValueError("Score must be between 0.0 and 1.0")
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"


def main():
    while True:
        try:
            score = float(input("Enter a score between 0.0 and 1.0: "))
            grade = get_grade(score)
            print(f"Grade: {grade}")
            break
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()