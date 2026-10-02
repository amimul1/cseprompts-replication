# ================= CSEPrompts manual cleaning =================
# task: codingsites/066 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given a knapsack weight W and a set of n items with certain value val[i] and weight wt[i], we
#   need to calculate the maximum amount that could make up this quantity exactly.
# ---- model response below: edit from here ----
def knapsack(W, wt, val, n):
    """
    This function solves the 0/1 knapsack problem using dynamic programming.

    Parameters:
    W (int): The maximum weight capacity of the knapsack.
    wt (list): A list of weights of the items.
    val (list): A list of values of the items.
    n (int): The number of items.

    Returns:
    int: The maximum value that can be put in a knapsack of capacity W.
    """
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]