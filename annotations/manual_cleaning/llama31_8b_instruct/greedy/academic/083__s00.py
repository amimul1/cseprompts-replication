# ================= CSEPrompts manual cleaning =================
# task: academic/083 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Your goal in this question is to create a playlist (that is, a list of songs) by your friend's
#   favorite artists.
#   #
#   #Write a function called playlist. playlist should have two parameters. The first parameter is a
#   dictionary, where the keys are band names and the values are song names. The second parameter is
#   a list of strings, where each string is an artist.
#   #
#   #playlist should return a list of all songs by the bands listed in the second parameter, sorted
#   alphabetically. If there are no matching artists, return "I guess I don't mind ads on the radio
#   that much"
#   #
#   #For example:
#   #artists_and_songs = {"Beyonce": ["Halo", "Run the World", "Irreplaceable"],\
#   #                     "Maroon 5": ["Sugar", "Payphone", "Memories"], "Harry Styles": \
#   #                     ["Sign of the Times", "Adore You", "Falling"], "AC/DC":\
#   #                     ["TNT", "It's a long way to the top", "Thunderstruck"]}
#   #friends_artists = ["Maroon 5", "AC/DC", "Tame Impala"]
#   #playlist(artists_and_songs, friends_artists) -> ["It's a long way to the top", "Memories",
#   "Payphone", "Sugar", "TNT", "Thunderstruck"]
# ---- model response below: edit from here ----
### Creating a Playlist Function
def playlist(artists_and_songs, friends_artists):
    """
    Creates a playlist of songs by the favorite artists.

    Args:
        artists_and_songs (dict): A dictionary where keys are band names and values are lists of song names.
        friends_artists (list): A list of strings representing the favorite artists.

    Returns:
        list: A list of songs by the favorite artists, sorted alphabetically. If no matching artists, returns a message.
    """

    # Initialize an empty list to store the songs
    playlist = []

    # Iterate over each artist in the list of favorite artists
    for artist in friends_artists:
        # Check if the artist exists in the dictionary
        if artist in artists_and_songs:
            # If the artist exists, add their songs to the playlist
            playlist.extend(artists_and_songs[artist])

    # If the playlist is empty, return a message
    if not playlist:
        return "I guess I don't mind ads on the radio that much"
    # Otherwise, return the sorted playlist
    else:
        return sorted(playlist)