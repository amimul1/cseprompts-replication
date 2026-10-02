# ================= CSEPrompts manual cleaning =================
# task: codingsites/065 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given a set of non-negative integers, and a value sum, determine if there is a subset of the
#   given set with sum equal to given sum.
# ---- model response below: edit from here ----
def subset_sum(nums, target_sum):
    """
    Determine if there is a subset of the given set with sum equal to the given sum.

    Args:
        nums (list): A list of non-negative integers.
        target_sum (int): The target sum.

    Returns:
        bool: True if a subset with the given sum exists, False otherwise.
    """
    n = len(nums)
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

    # Base case: sum 0 can be achieved with an empty subset
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    # The answer is stored in the bottom-right cell of the dp table
    return dp[n][target_sum]