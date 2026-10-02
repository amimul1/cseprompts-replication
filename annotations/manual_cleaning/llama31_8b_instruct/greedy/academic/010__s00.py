# ================= CSEPrompts manual cleaning =================
# task: academic/010 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show
#   nutrition information for the 20 most frequently consumed raw fruits … in the United States.
#   Retail stores are welcome to download the posters, print, display and/or distribute them to
#   consumers in close proximity to the relevant foods in the stores.”
#   
#   Implement a program that prompts consumers users to input a fruit (case-insensitively) and then
#   outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits,
#   which is also available as text. Capitalization aside, assume that users will input fruits
#   exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that
#   isn’t a fruit.
# ---- model response below: edit from here ----
# Define a dictionary with fruit names and their corresponding nutrition information
fruits = {
    "apple": {"calories": 95},
    "banana": {"calories": 105},
    "strawberries": {"calories": 50},
    "orange": {"calories": 60},
    "grapefruit": {"calories": 52},
    "kiwi": {"calories": 46},
    "peach": {"calories": 68},
    "pear": {"calories": 62},
    "watermelon": {"calories": 45},
    "plums": {"calories": 63},
    "apricot": {"calories": 17},
    "nectarine": {"calories": 62},
    "cherry": {"calories": 17},
    "grapes": {"calories": 60},
    "mango": {"calories": 55},
    "pineapple": {"calories": 82},
    "papaya": {"calories": 55},
    "pomegranate": {"calories": 105},
    "lemon": {"calories": 29},
    "lime": {"calories": 20},
    "tangerine": {"calories": 47}
}

def get_fruit_nutrition(fruit):
    """
    Returns the nutrition information for a given fruit.

    Args:
        fruit (str): The name of the fruit.

    Returns:
        dict: A dictionary containing the nutrition information for the fruit.
    """
    return fruits.get(fruit.lower())

def main():
    print("FDA Fruit Nutrition Poster Program")
    print("----------------------------------")

    while True:
        fruit = input("Enter a fruit (or 'quit' to exit): ")
        
        if fruit.lower() == 'quit':
            break

        nutrition_info = get_fruit_nutrition(fruit)
        if nutrition_info:
            print(f"One serving of {fruit} contains {nutrition_info['calories']} calories.")
        else:
            print(f"Sorry, we couldn't find any information for {fruit}.")

if __name__ == "__main__":
    main()
