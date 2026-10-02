# ================= CSEPrompts manual cleaning =================
# task: academic/013 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Suppose that you’re in the habit of making a list of items you need from the grocery store.
#   
#   Implement a program that prompts the user for items, one per line, until the user inputs
#   control-d (which is a common way of ending one’s input to a program). Then output the user’s
#   grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the
#   number of times the user inputted that item. No need to pluralize the items. Treat the user’s
#   input case-insensitively.
# ---- model response below: edit from here ----
# Create an empty dictionary to store the items and their counts
grocery_list = {}

# Continuously prompt the user for items until they input control-d
while True:
    try:
        item = input("Enter an item (or press Ctrl+D to finish): ")
    except EOFError:
        # If the user inputs control-d, break the loop
        break

    # Convert the item to lowercase for case-insensitive comparison
    item = item.lower()

    # If the item is already in the dictionary, increment its count
    if item in grocery_list:
        grocery_list[item] += 1
    # Otherwise, add the item to the dictionary with a count of 1
    else:
        grocery_list[item] = 1

# Sort the dictionary items alphabetically by key (item name)
sorted_items = sorted(grocery_list.items())

# Print the sorted list with the item count prefix
for item, count in sorted_items:
    print(f"{count} {item}")
