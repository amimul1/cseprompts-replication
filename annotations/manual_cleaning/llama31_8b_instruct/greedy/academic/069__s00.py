# ================= CSEPrompts manual cleaning =================
# task: academic/069 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called pivot_library. pivot_library takes
#   #as input one parameter, a list of 3-tuples. Each tuple in
#   #the list has three items: the first item is a book title
#   #(a string), the second item is the book's author (a
#   #string), and the third item is the book's ISBN number (a
#   #string).
#   #
#   #pivot_library should return a dictionary. In the dictionary
#   #that it returns, the keys should be the ISBN numbers, and
#   #the values should be 2-item tuples. In each tuple, the first
#   #item should be the book title, and the second item should
#   #be the author's name.
#   #
#   #Hint: Unpack the tuple to variables first, then create the
#   #new dictionary item.
#   #
#   #For example:
#   #
#   # books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
#   #          ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
#   # pivot_library(books)
#   #   -> {"978-0-140-17739-8": ("Of Mice and Men", "John Steinbeck"),
#   #       "978-1-260-08227-2": ("Introduction to Computing", "David Joyner")}
# ---- model response below: edit from here ----
def pivot_library(books):
    """
    This function takes a list of 3-tuples representing books and returns a dictionary.
    The dictionary has ISBN numbers as keys and tuples of book title and author as values.

    Args:
        books (list): A list of 3-tuples containing book information.

    Returns:
        dict: A dictionary with ISBN numbers as keys and tuples of book title and author as values.
    """
    # Initialize an empty dictionary to store the result
    result = {}

    # Iterate over each book in the input list
    for book in books:
        # Unpack the tuple into title, author, and ISBN variables
        title, author, isbn = book
        
        # Create a new dictionary item with the ISBN as the key and a tuple of title and author as the value
        result[isbn] = (title, author)

    # Return the resulting dictionary
    return result

# Example usage:
books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
         ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
print(pivot_library(books))
