# ================= CSEPrompts manual cleaning =================
# task: academic/012 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a
#   menu of entrees, per the dict below, wherein the value of each key is a price in dollars:
#   
#   {
#       "Baja Taco": 4.00,
#       "Burrito": 7.50,
#       "Bowl": 8.50,
#       "Nachos": 11.00,
#       "Quesadilla": 8.50,
#       "Super Burrito": 8.50,
#       "Super Quesadilla": 9.50,
#       "Taco": 3.00,
#       "Tortilla Salad": 8.00
#   }
#   Implement a program that enables a user to place an order, prompting them for items, one per
#   line, until the user inputs control-d (which is a common way of ending one’s input to a
#   program). After each inputted item, display the total cost of all items inputted thus far,
#   prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case
#   insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be
#   titlecased.
# ---- model response below: edit from here ----
# Define the menu
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize total cost and items ordered
total_cost = 0
items_ordered = []

while True:
    # Prompt user for input
    item = input("Enter an item to order (or Ctrl+D to finish): ")

    # Check if user wants to finish ordering
    if item == "":
        break

    # Convert input to title case
    item = item.title()

    # Check if item is in the menu
    if item in menu:
        # Add item to list of items ordered
        items_ordered.append(item)
        
        # Update total cost
        total_cost += menu[item]
        
        # Display total cost
        print(f"Total: ${total_cost:.2f}")
    else:
        print("Invalid item. Please try again.")

# Display final total and items ordered
print("\nFinal Order:")
for item in items_ordered:
    print(item)
print(f"Total: ${total_cost:.2f}")