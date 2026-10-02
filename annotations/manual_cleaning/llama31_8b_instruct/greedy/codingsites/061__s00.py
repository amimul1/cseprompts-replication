# ================= CSEPrompts manual cleaning =================
# task: codingsites/061 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   The Towers of Hanoi is a puzzle where we have three rods and n disks. The objective of the
#   puzzle is to move the entire stack to another rod. You are given the number of disks n.
#   Calculate the minimum number of moves needed to solve the puzzle.
# ---- model response below: edit from here ----
def towers_of_hanoi(n, from_rod, to_rod, aux_rod):
    """
    Recursive function to solve the Towers of Hanoi problem.

    Args:
        n (int): The number of disks.
        from_rod (str): The rod where the disks are initially stacked.
        to_rod (str): The rod where the disks need to be moved.
        aux_rod (str): The auxiliary rod.

    Returns:
        None
    """
    if n == 1:
        # Base case: Move a single disk from the from_rod to the to_rod.
        print(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
        return

    # Move n - 1 disks from the from_rod to the aux_rod, using the to_rod as auxiliary.
    towers_of_hanoi(n - 1, from_rod, aux_rod, to_rod)

    # Move the nth disk from the from_rod to the to_rod.
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")

    # Move the n - 1 disks from the aux_rod to the to_rod, using the from_rod as auxiliary.
    towers_of_hanoi(n - 1, aux_rod, to_rod, from_rod)


def min_moves(n):
    """
    Calculate the minimum number of moves required to solve the Towers of Hanoi problem.

    Args:
        n (int): The number of disks.

    Returns:
        int: The minimum number of moves.
    """
    return 2 ** n - 1