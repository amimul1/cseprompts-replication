# ================= CSEPrompts manual cleaning =================
# task: academic/039 | model: llama31_8b_instruct | run: greedy | sample: 0
# VARIABLES task: keep the whole script, including the variable assignments at the top.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   hot = True
#   cold = False
#   rainy = True
#   windy = False
#   snowy = False
#   
#   #You may modify the lines of code above, but don't move them!
#   #When you Submit your code, we'll change these lines to
#   #assign different values to the variables.
#   
#   #Earlier, you wrote a program that made clothing
#   #recommendations based on the weather. Your program could
#   #specifically recommend a jacket, boots, flip-flips, or a
#   #tshirt based on whether it was hot, cold, rainy, windy, or
#   #snowy.
#   #
#   #Let's add some accessories to that program: a hat, gloves,
#   #umbrella, and a scarf.
#   #
#   #Specifically, the program should recommend:
#   #
#   # - a hat if it's cold, or if it's hot but not rainy (cold
#   #   and rainy still means a hat, though).
#   # - gloves if it's cold and either snowy or rainy.
#   # - an umbrella if it's hot, snowy, or rainy.
#   # - a scarf if it's cold and windy or cold and snowy
#   #   unless it's rainy. Rain means no scarf regardless of
#   #   whether it's cold, windy, or snowy.
#   #
#   #Write some code below that will print four lines, one for
#   #each of the four types of clothing. The lines should look
#   #like this:
#   #
#   #Hat: True
#   #Gloves: True
#   #Umbrella: False
#   #Scarf: False
#   #
#   #The values (True and False) will differ based on the
#   #values assigned to hot, cold, windy, snowy, and rainy
#   #at the start of the program.
#   
#   
#   #Add your code here!
# ---- model response below: edit from here ----
hot = True
cold = False
rainy = True
windy = False
snowy = False

# Define a function to make clothing recommendations
def make_recommendations(hot, cold, rainy, windy, snowy):
    # Initialize variables to store recommendations
    hat = False
    gloves = False
    umbrella = False
    scarf = False

    # Check for hat recommendation
    if cold or (hot and not rainy):
        hat = True

    # Check for gloves recommendation
    if cold and (rainy or snowy):
        gloves = True

    # Check for umbrella recommendation
    if hot or snowy or rainy:
        umbrella = True

    # Check for scarf recommendation
    if cold and windy and not rainy:
        scarf = True
    elif cold and snowy and not rainy:
        scarf = True

    # Print the recommendations
    print(f"Hat: {hat}")
    print(f"Gloves: {gloves}")
    print(f"Umbrella: {umbrella}")
    print(f"Scarf: {scarf}")

# Call the function with the given weather conditions
make_recommendations(hot, cold, rainy, windy, snowy)