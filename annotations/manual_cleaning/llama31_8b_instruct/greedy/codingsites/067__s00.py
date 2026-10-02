# ================= CSEPrompts manual cleaning =================
# task: codingsites/067 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given a value N, if we want to make change for N cents, and we have infinite supply of each of S
#   = { S1, S2, .. , Sm} valued coins, how many ways can we make the change?
# ---- model response below: edit from here ----
def num_ways_to_make_change(N, S):
    """
    Calculate the number of ways to make change for N cents using coins of denominations S.

    Args:
        N (int): The total amount to make change for.
        S (list): A list of coin denominations.

    Returns:
        int: The number of ways to make change for N cents.
    """
    # Create a list to store the number of ways to make change for each amount from 0 to N
    ways = [0] * (N + 1)
    ways[0] = 1  # There is 1 way to make change for 0 cents (no coins)

    # For each coin denomination
    for s in S:
        # For each amount from the coin denomination to N
        for i in range(s, N + 1):
            # The number of ways to make change for the current amount is the sum of the number of ways to make change for the current amount without using the current coin and the number of ways to make change for the amount minus the current coin
            ways[i] += ways[i - s]

    return ways[N]