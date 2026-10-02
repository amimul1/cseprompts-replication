# ================= CSEPrompts manual cleaning =================
# task: academic/094 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #In volleyball, the first team to score 25 points wins.
#   #However, they must win by 2. So, if the score is 25-24,
#   #they keep playing until someone is ahead by 2 points.
#   #
#   #Write a function called check_volleyball_winner. This
#   #function will take as input a 2-tuple of two integers: the
#   #first integer is Team 1's score, and the second integer
#   #is Team 2's score. check_volleyball_winner should return a
#   #string:
#   #
#   # - If Team 1 has won, return "Team 1 wins!"
#   # - If Team 2 has won, return "Team 2 wins!"
#   # - If neither player has won, return "Keep playing!"
#   #
#   #For example:
#   # check_volleyball_winner((23, 17)) -> "Keep playing!"
#   # check_volleyball_winner((25, 17)) -> "Team 1 wins!"
#   # check_volleyball_winner((23, 25)) -> "Team 2 wins!"
#   # check_volleyball_winner((25, 24)) -> "Keep playing!"
#   # check_volleyball_winner((29, 29)) -> "Keep playing!"
#   # check_volleyball_winner((29, 30)) -> "Keep playing!"
#   # check_volleyball_winner((29, 31)) -> "Team 2 wins!"
#   #
#   #Remember, the function should RETURN these strings, not
#   #print them.
# ---- model response below: edit from here ----
### Volleyball Winner Checker Function
def check_volleyball_winner(score):
    """
    Checks the winner of a volleyball game.

    Args:
        score (tuple): A 2-tuple of two integers representing the scores of Team 1 and Team 2.

    Returns:
        str: A string indicating the winner of the game or a message to keep playing.
    """
    team1_score, team2_score = score

    # Check if Team 1 has won
    if team1_score >= 25 and team1_score - team2_score >= 2:
        return "Team 1 wins!"

    # Check if Team 2 has won
    elif team2_score >= 25 and team2_score - team1_score >= 2:
        return "Team 2 wins!"

    # If neither team has won, return a message to keep playing
    else:
        return "Keep playing!"