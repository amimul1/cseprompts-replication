# ================= CSEPrompts manual cleaning =================
# task: academic/003 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   implement a program that prompts the user for the name of a file and then outputs that file’s
#   media type if the file’s name ends, case-insensitively, in any of these suffixes:
#   
#   .gif
#   .jpg
#   .jpeg
#   .png
#   .pdf
#   .txt
#   .zip
#   If the file’s name ends with some other suffix or has no suffix at all, output
#   application/octet-stream instead, which is a common default.
# ---- model response below: edit from here ----
def get_media_type(filename):
    """
    Returns the media type of a file based on its suffix.

    Args:
        filename (str): The name of the file.

    Returns:
        str: The media type of the file.
    """
    suffixes = ['.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip']
    filename = filename.lower()
    for suffix in suffixes:
        if filename.endswith(suffix):
            return 'image/' + suffix[1:]
    return 'application/octet-stream'

def main():
    filename = input("Enter the name of the file: ")
    media_type = get_media_type(filename)
    print(f"The media type of the file is: {media_type}")

if __name__ == "__main__":
    main()