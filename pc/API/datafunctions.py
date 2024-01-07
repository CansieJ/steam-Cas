import steamAPI_functions as API
from ProjectSteam.pc.API import bubbleSort
import json

try:
    a = open("../storage/steam.json")
except:
    a = open("storage/steam.json")
data = json.load(a)


def getTopGames(amount):
    games = API.getOwnedGames()
    playtimeList = []
    for item in games:
        playtimeList.append([item["playtime_forever"], item["appid"]])
    result = bubbleSort.bubble(playtimeList, 0, reverse=True)
    return result[:amount]


# print(getTopGames(3))


def nameget(id):
    for item in data:
        if item["appid"] == id:
            return item["name"]


# print(nameget(10))


def friendGames():
    friends = API.getFriendList()
    fgames = []
    for item in friends:
        games = API.getOwnedGames(item)
        glijst = []
        for item in games:
            glijst.append(item["appid"])
        fgames.append(glijst)
    return fgames


# print(friendGames())


def unshared_games(repeat=True, count=False, list=False):
    mijngames = API.getOwnedGames(API.steamID)
    fgames = friendGames()
    unshared = []
    if repeat == True:
        for item in fgames:
            for subitem in item:
                if subitem not in mijngames:
                    unshared.append(subitem)
    if repeat == False:
        for item in fgames:
            for subitem in item:
                if subitem not in mijngames and subitem not in unshared:
                    unshared.append(subitem)
    if count == True:
        unshared2 = []
        games1x = []
        for item in unshared:
            if item not in games1x:
                games1x.append(item)
        for item in games1x:
            counter = 0
            for item2 in unshared:
                if item == item2:
                    counter += 1
            if list == False:
                unshared2.append(f"{counter} {item}")
            if list == True:
                unshared.append([counter, item])
        return unshared2
    if count == False:
        return unshared


# print(unshared_games(repeat=True,count=True,list=True))
# repeat zorgt ervoor dat als meerdere vrienden dezelfde game hebben dat het zo vaak voor komt
# count telt hoeveel vrienden dezelfde game hebben
# list returned count als een lijst ipv als 1 element
