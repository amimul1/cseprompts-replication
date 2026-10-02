# ================= CSEPrompts manual cleaning =================
# task: codingsites/062 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given weights and values of n items, put these items in a knapsack of capacity W to get the
#   maximum total value in the knapsack.
# ---- model response below: edit from here ----
def knapsack(weights, values, capacity):
    """
    Solves the 0/1 knapsack problem using dynamic programming.

    Parameters:
    weights (list): List of weights of items
    values (list): List of values of items
    capacity (int): Maximum capacity of the knapsack

    Returns:
    max_value (int): Maximum total value that can be put in the knapsack
    items (list): List of items to include in the knapsack
    """
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]
    items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items.append(i - 1)
            w -= weights[i - 1]

    return max_value, items[::-1]