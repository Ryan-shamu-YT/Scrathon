import json
import random
import os
from code import encode
from code import decode

def getToken(username, password):
    username = username.lower()
    with open("account_index.json", "r") as file:
        account_index_json = json.load(file)

    with open("account.json", "r") as file:
        account_json = json.load(file)

    if username in account_index_json:
        index = account_index_json.index(username)
        TOKEN = decode(password, account_json[index]['Acc'][0])
        passwordTest = decode(password, account_json[index]['Acc'][1])
        result = [TOKEN, passwordTest]
    else:
        return "False"

    return result


def setToken(username, password):
    username = username.lower()
    result = ["False"]
    with open("account_index.json", "r") as file:
        account_index_json = json.load(file)

    with open("account.json", "r") as file:
        account_json = json.load(file)

    if username not in account_index_json:
        account_index_json.append(username)
        result = ["True"]
        TOKEN_random = random.randint(
            9999999999999999999999999999999999999999999999999999,
            99999999999999999999999999999999999999999999999999999)
        with open("TOKEN.json", "r") as file:
            TOKEN_list = json.load(file)
        while TOKEN_random in TOKEN_list:
            TOKEN_random = random.randint(
                9999999999999999999999999999999999999999999999999999,
                99999999999999999999999999999999999999999999999999999)
        result.append(TOKEN_random)

        TOKEN_list.append(TOKEN_random)

        with open("TOKEN.json", "w") as file:
            json.dump(TOKEN_list, file)

        TOKEN = encode(password, TOKEN_random)
        key = encode(password, os.environ['testkey'])
        account_json.append({'Acc': [TOKEN, key]})

    with open("account_index.json", "w") as file:
        json.dump(account_index_json, file)

    with open("account.json", "w") as file:
        json.dump(account_json, file)

    return result


def AccountExist(username):
    with open("account_index.json", "r") as file:
        data = json.load(file)
    if username.lower() in data:
        return "True"
    return "False"