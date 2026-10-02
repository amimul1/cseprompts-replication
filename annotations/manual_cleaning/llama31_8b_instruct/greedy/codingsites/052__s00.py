# ================= CSEPrompts manual cleaning =================
# task: codingsites/052 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   The aim of this challenge is to write a function that determines who is online, offline and
#   away. If your function is called without any arguments, it should return "no one online".
# ---- model response below: edit from here ----
### User Status Function
class User:
    def __init__(self, name):
        self.name = name
        self.status = "offline"

    def update_status(self, status):
        self.status = status

def get_user_status(users):
    online_users = [user for user in users if user.status == "online"]
    away_users = [user for user in users if user.status == "away"]
    offline_users = [user for user in users if user.status == "offline"]

    if online_users:
        return f"{', '.join([user.name for user in online_users])} are online, {', '.join([user.name for user in away_users])} are away, {', '.join([user.name for user in offline_users])} are offline"
    else:
        return "no one online"