# ================= CSEPrompts manual cleaning =================
# task: academic/097 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #The game Uno is a card game where each player's goal is
#   #to get rid of all their cards. A round ends when one player
#   #has gotten rid of all their cards. They then receive a
#   #number of points based on the cards left in their opponents'
#   #hands. The first player to reach 500 points across multiple
#   #rounds wins the game.
#   #
#   #Write a function called check_uno_winner. This function will
#   #take as input a tuple with at least 2 integers, but up to 8.
#   #Each integer will represent one player's score.
#   #
#   #If any player has more than 500 points, check_uno_winner
#   #should return the string, "Player X wins!", where X refers
#   #to the position of the player in the list who has more than
#   #500 points. Because Uno is played in the real world, the
#   #first player in the list should be referred to as Player 1,
#   #the second player as Player 2, and so on.
#   #
#   #If no player has more than 500 points, check_uno_winner
#   #should return the string, "Keep playing!"
#   #
#   #For example:
#   # check_uno_winner((0, 0)) -> "Keep playing!"
#   # check_uno_winner((505, 250)) -> "Player 1 wins!"
#   # check_uno_winner((250, 505)) -> "Player 2 wins!"
#   # check_uno_winner((25, 101, 362, 415)) -> "Keep playing!"
#   # check_uno_winner((25, 101, 426, 515)) -> "Player 4 wins!"
#   #
#   #Remember, the function should RETURN these strings, not
#   #print them. You may assume that only one player will have
#   #a score above 500.
# ---- model response below: edit from here ----
def check_uno_winner(scores):
    """
    This function determines the winner of a game of Uno based on the scores of the players.

    Args:
        scores (tuple): A tuple containing the scores of the players.

    Returns:
        str: A string indicating whether a player has won the game or if the game should continue.
    """
    for i, score in enumerate(scores, start=1):
        if score > 500:
            return f"Player {i} wins!"
    return "Keep playing!"
