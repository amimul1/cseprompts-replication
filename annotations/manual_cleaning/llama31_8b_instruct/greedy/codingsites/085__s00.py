# ================= CSEPrompts manual cleaning =================
# task: codingsites/085 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   When users post an update on social media,such as a URL, image, status update etc., other users
#   in their network are able to view this new post on their news feed. Users can also see exactly
#   when the post was published, i.e, how many hours, minutes or seconds ago. Given two timestamps
#   of one such post, one in Mon DD YYYY hh:mm:ss +ZZZZZ format and the other in Day, DD Mon YYYY
#   hh:mm:ss +ZZZZZ format, print the absolute difference (in seconds) between them.
# ---- model response below: edit from here ----
from datetime import datetime

def calculate_timestamp_diff(timestamp1, timestamp2):
    """
    Calculate the absolute difference between two timestamps in seconds.

    Args:
        timestamp1 (str): The first timestamp in 'Mon DD YYYY hh:mm:ss +ZZZZZ' format.
        timestamp2 (str): The second timestamp in 'Day, DD Mon YYYY hh:mm:ss +ZZZZZ' format.

    Returns:
        int: The absolute difference between the two timestamps in seconds.
    """

    # Parse the timestamps into datetime objects
    dt1 = datetime.strptime(timestamp1, '%a %d %b %Y %H:%M:%S %z')
    dt2 = datetime.strptime(timestamp2, '%a %d %b %Y %H:%M:%S %z')

    # Calculate the absolute difference between the two timestamps
    diff = abs((dt2 - dt1).total_seconds())

    return int(diff)