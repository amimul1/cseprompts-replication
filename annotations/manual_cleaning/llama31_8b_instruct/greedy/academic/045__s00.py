# ================= CSEPrompts manual cleaning =================
# task: academic/045 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   message = "lol"
#   punct = "!"
#   num = 3
#   
#   #You may modify the lines of code above, but don't move them!
#   #When you Submit your code, we'll change these lines to
#   #assign different values to the variables.
#   
#   #Using the values of message, punct, and num, print
#   #a string that looks like the one below if message = "lol",
#   #punct = "!", and num = 3:
#   #
#   # !!!lollollol!!!lollollol!!!lollollol!!!
#   #
#   #Specifically, it should start by printing punct num
#   #times, then print message num times, repeat that entire
#   #process num times, and then print punct num times
#   #again.
#   #
#   #Here are a couple other examples:
#   #
#   # message = "bbl", punct = ":", num = 1 -> :bbl:
#   # message = "bbq", punct = "?", num = 2 -> "??bbqbbq??bbqbbq??
#   # message = "brb", punct = ".", num = 4 ->
#   ....brbbrbbrbbrb....brbbrbbrbbrb....brbbrbbrbbrb....brbbrbbrbbrb....
# ---- model response below: edit from here ----
message = "lol"
punct = "!"
num = 3

# Print punct num times
print(punct * num)

# Print message num times, repeat num times
for _ in range(num):
    print(message * num)

# Print punct num times
print(punct * num)
