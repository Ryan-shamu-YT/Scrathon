import os
import scratchattach as scratch3
import json
import requests
from urllib import request as request_url

# --- account.py ---

from account import getToken
from account import setToken
from account import AccountExist

# --- System.py ---

from System import getInfo

# --- coin_interaction.py ---

from coin_interaction import addCoin
from coin_interaction import removeCoin
from coin_interaction import getCoinAmount

# --- connecting ... ---

print("connecting:")
json_file = "Settings.json"
USERNAME_login = getInfo("USERNAME", json_file)
print("Username:" + USERNAME_login)
PROJECT_ID_login = getInfo("Project_id", json_file)
print("Project id:" + PROJECT_ID_login)
testkey = os.environ['testkey']
SESSION_ID = os.environ['session_id']
conn = scratch3.CloudConnection(project_id=PROJECT_ID_login,
                                username=USERNAME_login,
                                session_id=SESSION_ID)
variables = scratch3.get_cloud(PROJECT_ID_login)
client = scratch3.CloudRequests(conn)
print("connected")

# --- script ---


@client.request
def ping():
    print("Ping request received")
    return "pong"


@client.request
def Userinfo(argument1):
    user = scratch3.get_user(argument1)
    user.update()

    follower = user.follower_count()
    user_project_count = user.project_count()
    user_fav_projects = user.favorites_count()
    curating_studios = user.studio_count()
    message_count = user.message_count()
    studio_following = user.studio_following_count()
    joined = user.join_date
    country = user.country

    with open("Index.json", "r") as file:
        getIndex = json.load(file)

    i = getIndex.index(argument1.lower())

    with open("coins.json", "r") as file:
        getCoins = json.load(file)

    Info = getCoins[i][argument1.lower()]["Coins"]

    data = [follower, user_project_count, user_fav_projects, curating_studios, message_count, studio_following, joined, country, Info]
    return data


@client.request
def Register(argument1):
    print(f"Data requested for user {argument1.lower()}")
    filename = 'coins.json'

    with open(filename, "r") as file:
        data = json.load(file)

    with open("Index.json", "r") as file:
        data2 = json.load(file)

    registered = False
    if argument1.lower() not in data2:
        registered = True
        with open("Settings.json", "r") as file:
            data_2 = json.load(file)
        data_3 = data_2[0]
        SCoins = data_3["start_coins"]
        entry = {argument1.lower(): {"Coins": SCoins}}
        data.append(entry)
        data2.append(argument1.lower())
        with open("Index.json", "w") as file:
            json.dump(data2, file)

    with open(filename, "w") as file:
        json.dump(data, file)
    with open("backup-coins.json", "w") as file:
        json.dump(data, file)

    return registered


@client.request
def IsRegistered(argument1):
    result = False
    with open("Index.json", "r") as file:
        index = json.load(file)
    if argument1.lower() in index:
        result = True
    return result


@client.request
def payCoin(argument1, argument2):
    arg1 = argument1.split('§')[0].lower()  # username
    arg2 = argument1.split('§')[1].lower()  # accountname
    arg3 = argument1.split('§')[2]  # TOKEN
    arg4 = argument2.split('§')[0].lower()  # user to pay to
    arg5 = argument2.split('§')[1]  # amount
    arg6 = argument2.split('§')[2]  # password

    result = False

    print("-----------" + "\n" + arg1 + "\n" + arg2 + "\n" + arg3 + "\n" +
          arg4 + "\n" + arg5 + "\n" + "-----------")

    if int(getCoinAmount(arg2)) >= int(arg5):
        print(True)
        if getToken(arg2, arg6)[1] == testkey:
            print(True)
            if int(getToken(arg2, arg6)[0]) == int(arg3):
                print(True)
                removeCoin(arg2, arg5)
                addCoin(arg4, arg5)
                result = True

    return result


@client.request
def checkToken(argument1, argument2):
    print(getToken(argument1, argument2))
    if getToken(argument1, argument2)[1] == testkey:
        return ["True", getToken(argument1, argument2)[0]]
    return False


@client.request
def RegisterAcc(argument1, argument2):
    return setToken(argument1, argument2)


@client.request
def registeredList():
    with open("Index.json", "r") as file:
        data = json.load(file)
    return data


@client.event
def on_ready():
    print("Request handler is ready")


@client.request
def IsAccRegistered(username):
    return AccountExist(username)


client.run()
