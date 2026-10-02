# ================= CSEPrompts manual cleaning =================
# task: academic/072 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #In the game tic-tac-toe, two players take turns drawing
#   #Xs and Os on a 3x3 grid. If one player can place three of
#   #their symbols side-by-side in a row, column, or diagonal,
#   #they win the game.
#   #
#   #For example:
#   #
#   # X Wins:   X Wins:   X Wins:   No Winner:
#   # X|O|X     O|X|X     O|O|      X|O|O
#   # -+-+-     -+-+-     -+-+-     -+-+-
#   # O|O|X     X|O|      X|X|X     O|X|X
#   # -+-+-     -+-+-     -+-+-     -----
#   # O|X|X      | |O      | |      X|X|O
#   #
#   #Write a function called check_winner. check_winner will
#   #take one parameter as input, a 2D tuple (that is, a tuple
#   #of tuples). The 2D tuple represents the game board: each
#   #smaller tuple in the larger tuple is a row of the board,
#   #and each item in the smaller tuple is a spot on the
#   #board. There will always be three tuples in the larger
#   #tuple, and three items in each of the smaller tuples.
#   #
#   #Each item in the smaller tuple will always be one of three
#   #values: the string "X", the string "O", or the value None.
#   #
#   #check_winner should return one of three values: the string
#   #"X" if X has won the game; the string "O" if O has won the
#   #game; or the value None if there is no winner. None should
#   #NOT be the string "None"; it should be the value None,
#   #like the boolean values True and False.
#   #
#   #You may assume a player has won the game if and only if
#   #the board has three of their symbols in a row: you do not
#   #need to worry about whether the input is a valid game
#   #otherwise (e.g. a board of nine Xs still counts as X
#   #winning). You may assume that there will only be one
#   #winner per board.
#   #
#   #Hint: There are only eight possible places to win (three
#   #rows, three columns, two diagonals).
#   #
#   #Hint 2: If you're comfortable on time, you may want to
#   #check out the last problem before doing this one. It's
#   #only worth 1 point, but you might be able to design
#   #one solution that works for both problems!
# ---- model response below: edit from here ----
def check_winner(board):
    """
    Checks for a winner in a Tic Tac Toe game.

    Args:
        board (tuple of tuples): A 2D tuple representing the game board.

    Returns:
        str or None: The winner of the game ("X" or "O") or None if there is no winner.
    """

    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # If no winner is found, return None
    return None