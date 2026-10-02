# ================= CSEPrompts manual cleaning =================
# task: codingsites/064 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   You are given two identical eggs and you have access to a building with n floors. What is the
#   minimum number of trials you need to find the highest floor from which the egg can be dropped
#   without breaking?
# ---- model response below: edit from here ----
def egg_drop(n):
    """
    Calculate the minimum number of trials needed to find the highest floor from which the egg can be dropped without breaking.

    Args:
        n (int): The number of floors in the building.

    Returns:
        int: The minimum number of trials needed.
    """
    # Create a table to store the results of subproblems
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Initialize the base cases
    for i in range(1, n + 1):
        dp[1][i] = i

    # Fill the table in a bottom-up manner
    for eggs in range(2, n + 1):
        for x in range(1, n + 1):
            # Initialize the minimum number of trials for the current subproblem
            min_trials = float('inf')
            for j in range(1, x + 1):
                # Calculate the number of trials for the current subproblem
                trials = 1 + max(dp[eggs - 1][j - 1], dp[eggs][x - j])
                # Update the minimum number of trials
                min_trials = min(min_trials, trials)
            # Store the result in the table
            dp[eggs][x] = min_trials

    # The minimum number of trials for the original problem is stored in the last cell of the table
    return dp[2][n]
