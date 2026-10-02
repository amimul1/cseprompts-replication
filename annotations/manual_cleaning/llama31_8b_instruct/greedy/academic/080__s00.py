# ================= CSEPrompts manual cleaning =================
# task: academic/080 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #In the game Rock-Paper-Scissors, two opponents
#   #simultaneously choose to throw either "Rock", "Paper",
#   #or "Scissors". Rock beats Scissors, Scissors beats Paper,
#   #and Paper beats Rock. If both players throw the same
#   #object, the round is a tie.
#   #
#   #Write a function called find_winner. find_winner will take
#   #as input a list of 2-tuples, each representing a round of
#   #Rock-Paper-Scissors. Each 2-tuple will contain two strings.
#   #Each string will be either "Rock", "Paper", or "Scissors".
#   #The first item in the 2-tuple will represent what Player 1
#   #chooses in each round, and the second item in the 2-tuple
#   #will represent what Player 2 chooses in each round.
#   #
#   #find_winner should return the string "Player 1 wins!" if
#   #Player 1 wins more games than Player 2. It should return the
#   #string "Player 2 wins!" if Player 2 wins more games than
#   #Player 1. It should return the string "It's a tie!" if the
#   #two players win an equal number of times.
#   #
#   #The number of times the two players tie is irrelevant to the
#   #result: all that matters is who wins more rounds than the
#   #other.
#   #
#   #For example:
#   #
#   # find_winner([("Rock", "Rock"), ("Rock", "Scissors"),
#   #              ("Paper", "Rock"), ("Scissors", "Rock")])
#   #
#   #...would return "Player 1 wins!" because Player 1 wins
#   #two round and Player 2 wins one round.
# ---- model response below: edit from here ----
def find_winner(rounds):
    """
    Determine the winner of a Rock-Paper-Scissors game given a list of rounds.

    Args:
        rounds (list): A list of 2-tuples, each representing a round of Rock-Paper-Scissors.
            Each 2-tuple contains two strings, representing the choices of Player 1 and Player 2.

    Returns:
        str: The string "Player 1 wins!" if Player 1 wins more games than Player 2,
            "Player 2 wins!" if Player 2 wins more games than Player 1,
            "It's a tie!" if the two players win an equal number of times.
    """

    # Initialize counters for Player 1 and Player 2 wins
    player1_wins = 0
    player2_wins = 0

    # Iterate over each round
    for player1_choice, player2_choice in rounds:
        # Check who wins this round
        if player1_choice == player2_choice:
            # If both players choose the same, it's a tie
            continue
        elif (player1_choice == "Rock" and player2_choice == "Scissors") or \
             (player1_choice == "Scissors" and player2_choice == "Paper") or \
             (player1_choice == "Paper" and player2_choice == "Rock"):
            # Player 1 wins this round
            player1_wins += 1
        else:
            # Player 2 wins this round
            player2_wins += 1

    # Determine the winner
    if player1_wins > player2_wins:
        return "Player 1 wins!"
    elif player2_wins > player1_wins:
        return "Player 2 wins!"
    else:
        return "It's a tie!"