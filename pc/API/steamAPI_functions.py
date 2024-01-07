from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()
apikey = os.environ.get("STEAM_API_KEY")
steamID = os.environ.get("STEAMID")


def getPlayerSummaries(steamids):
    uri = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={apikey}&steamids={steamids}"
    r = requests.get(uri)
    print("Status GetPlayerSummaries():", r.status_code)

    data = r.json()
    # summaries = []
    # for player in data["response"]["players"]:
    #     summaries.append(player)

    return data


def getFriendList():
    uri = f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={apikey}&steamid={steamID}&relationship=friend"
    r = requests.get(uri)
    print("Status getFriendsList():", r.status_code)

    data = r.json()

    for friend in data["friendslist"]["friends"]:
        friend |= getPlayerSummaries(friend["steamid"])

    with open("storage/myFriends.json", "w") as f:
        json.dump(data, f, indent=6)
    # friendList = []
    # for friend in data["friendslist"]["friends"]:
    #     friendList.append(friend["steamid"])

    # return friendList


def getOwnedGames(id):
    uri = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={apikey}&steamid={id}&format=json"
    r = requests.get(uri)
    print("Status getOwnedGames():", r.status_code)

    data = r.json()
    with open("storage/myGames.json", "w") as f:
        json.dump(data, f, indent=6)

    # gamesList = []
    # for game in data["response"]["games"]:
    #     if game["playtime_forever"] > 0:
    #         gamesList.append(game)

    # return gamesList


def getRecentlyPlayedGames():
    uri = f"https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={apikey}&steamid={steamID}&format=json"
    r = requests.get(uri)
    print("Status getRecentlyPlayedGames():", r.status_code)

    data = r.json()
    games = []

    if data["response"]["total_count"] > 0:
        for game in data["response"]["games"]:
            games.append(game)

    return games


def getUserStatsForGame(appid):
    uri = f"https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={appid}&key={apikey}&steamid={steamID}"
    r = requests.get(uri)
    print("Status getUserStatsForGame():", r.status_code)

    data = r.json()
    achievements = []
    stats = []

    if "stats" in data["playerstats"]:
        for stat in data["playerstats"]["stats"]:
            stats.append(stat)
    if "achievements" in data["playerstats"]:
        for achievement in data["playerstats"]["achievements"]:
            achievements.append(achievement)

    return achievements, stats


def getGlobalAchievementPercentages(appid):
    uri = f"https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={appid}&format=jfon"
    r = requests.get(uri)
    print("Status getGlobalAchievementPercentages():", r.status_code)

    data = r.json()
    percentages = []
    for achievement in data["achievementpercentages"]["achievements"]:
        percentages.append(achievement)

    return percentages
