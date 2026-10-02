# ================= CSEPrompts manual cleaning =================
# task: codingsites/083 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Kevin and Stuart want to play the 'The Minion Game'. Game Rules: Both players are given the same
#   string, S. Both players have to make substrings using the letters of the string S. Stuart has to
#   make words starting with consonants. Kevin has to make words starting with vowels. The game ends
#   when both players have made all possible substrings. A player gets +1 point for each occurrence
#   of the substring in the string S.
# ---- model response below: edit from here ----
def minion_game(s):
    """
    Calculate the score for Kevin and Stuart in the Minion Game.

    Parameters:
    s (str): The input string.

    Returns:
    tuple: A tuple containing the scores for Kevin and Stuart.
    """
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    n = len(s)

    for i in range(n):
        if s[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    return kevin_score, stuart_score


def main():
    s = input("Enter the string: ")
    kevin_score, stuart_score = minion_game(s)
    print("Kevin's score:", kevin_score)
    print("Stuart's score:", stuart_score)

    if kevin_score > stuart_score:
        print("Kevin wins!")
    elif stuart_score > kevin_score:
        print("Stuart wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()