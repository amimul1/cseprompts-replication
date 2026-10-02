# ================= CSEPrompts manual cleaning =================
# task: academic/085 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #In ping-pong (table tennis), the first person to score 21
#   #points wins. However, they must win by 2. So, if the score
#   #is 21-20, they keep playing until someone is ahead by 2
#   #points.
#   #
#   #Write a function called check_pingpong_winner. This
#   #function will take as input a 2-tuple of two integers: the
#   #first integer is Player 1's score, and the second integer
#   #is Player 2's score. check_pingpong_winner should return a
#   #string:
#   #
#   # - If Player 1 has won, return "Player 1 wins!"
#   # - If Player 2 has won, return "Player 2 wins!"
#   # - If neither player has won, return "Keep playing!"
#   #
#   #For example:
#   # check_pingpong_winner((19, 13)) -> "Keep playing!"
#   # check_pingpong_winner((21, 13)) -> "Player 1 wins!"
#   # check_pingpong_winner((19, 21)) -> "Player 2 wins!"
#   # check_pingpong_winner((21, 20)) -> "Keep playing!"
#   # check_pingpong_winner((25, 25)) -> "Keep playing!"
#   # check_pingpong_winner((25, 27)) -> "Player 2 wins!"
#   #
#   #Remember, the function should RETURN these strings, not
#   #print them.
# ---- model response below: edit from here ----
def check_pingpong_winner(scores):
    """
    Checks the winner of a ping-pong game.

    Args:
        scores (tuple): A 2-tuple of two integers representing the scores of Player 1 and Player 2.

    Returns:
        str: A string indicating the winner of the game or a message to keep playing.
    """
    player1_score, player2_score = scores

    # Check if Player 1 has won
    if player1_score >= 21 and player1_score - player2_score >= 2:
        return "Player 1 wins!"

    # Check if Player 2 has won
    elif player2_score >= 21 and player2_score - player1_score >= 2:
        return "Player 2 wins!"

    # If neither player has won, return a message to keep playing
    else:
        return "Keep playing!"