import json
import sys

sys.path.insert(1, "../src/steamAPI")
import API.steamAPI_functions as API


def achievements(appid, mode="achievements"):
    result = API.getUserStatsForGame(appid)
    lijst = []

    if mode == "achievements" or mode == "both":
        for entry in result[0]:
            lijst.append(f"{str(entry['name'])}: {bool(entry['achieved'])}\n")
    if mode == "stats" or mode == "both":
        for entry in result[1]:
            lijst.append(f"{str(entry['name'])}: {entry['value']}\n")

    for x in lijst:
        print(x)
    return lijst


def friendlist():
    friends = []
    with open("storage/myFriends.json", "r") as f:
        data = json.load(f)
        for friend in data["friendslist"]["friends"]:
            name = friend["response"]["players"][0]["personaname"]
            online = "Niet Online"
            if friend["response"]["players"][0]["personastate"] == 1:
                online = "Online"
            friends.append(f"{name}, {online}\n")
    return friends


def refreshFriendList():
    API.getFriendList()
