# ================= CSEPrompts manual cleaning =================
# task: academic/078 | model: llama31_8b_instruct | run: greedy | sample: 0
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
#   #the values should be new dictionaries. Each new dictionary
#   #should have two keys: "title" and "author". Their values
#   #should correspond to the first and second items from the
#   #original 3-tuple.
#   #
#   #For example:
#   #
#   # books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
#   #          ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
#   # pivot_library(books)
#   #   -> {"978-0-140-17739-8": {"title": "Of Mice and Men", "author": "John Steinbeck"},
#   #       "978-1-260-08227-2": {"title": "Introduction to Computing", "author": "David Joyner"}}
# ---- model response below: edit from here ----
def pivot_library(books):
    """
    This function takes a list of 3-tuples representing books and returns a dictionary.
    The dictionary has ISBN numbers as keys and dictionaries with "title" and "author" as values.

    Args:
        books (list): A list of 3-tuples containing book information.

    Returns:
        dict: A dictionary with ISBN numbers as keys and dictionaries with "title" and "author" as values.
    """
    # Initialize an empty dictionary to store the result
    result = {}

    # Iterate over each book in the input list
    for book in books:
        # Extract the ISBN, title, and author from the tuple
        isbn, title, author = book

        # Create a new dictionary with the title and author
        book_info = {"title": title, "author": author}

        # Add the book information to the result dictionary
        result[isbn] = book_info

    # Return the result dictionary
    return result
