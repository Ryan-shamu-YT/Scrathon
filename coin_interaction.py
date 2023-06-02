import json

def addCoin(argument1, argument2):
    with open("Index.json", "r") as file:
        data = json.load(file)
    if argument1.lower() in data:
        with open("coins.json", "r") as file:
            data2 = json.load(file)

        data9 = data.index(argument1.lower())

        data3 = data2[data9]
        data4 = data3[argument1.lower()]
        data5 = data4['Coins']
        data6 = data5 + int(argument2)
        data7 = data.index(argument1.lower())
        data2.insert(data7, {argument1.lower(): {'Coins': data6}})
        data9 = data.index(argument1.lower())

        data10 = data9 + 1

        data2.remove(data2[data10])
        with open("coins.json", "w") as file:
            json.dump(data2, file)
        with open("backup-coins.json", "w") as file:
            json.dump(data2, file)
        print(argument1.lower() + ':' + str(data6))
        return argument1.lower() + ':' + str(data6)


def removeCoin(argument1, argument2):
    with open("Index.json", "r") as file:
        data = json.load(file)
    if argument1.lower() in data:
        with open("coins.json", "r") as file:
            data2 = json.load(file)

        data9 = data.index(argument1.lower())

        data3 = data2[data9]
        data4 = data3[argument1.lower()]
        data5 = data4['Coins']
        data6 = data5 - int(argument2)
        data7 = data.index(argument1.lower())
        data2.insert(data7, {argument1.lower(): {'Coins': data6}})
        data9 = data.index(argument1.lower())

        data10 = data9 + 1

        data2.remove(data2[data10])
        with open("coins.json", "w") as file:
            json.dump(data2, file)
        with open("backup-coins.json", "w") as file:
            json.dump(data2, file)
        print(argument1.lower() + ':' + str(data6))
        return argument1.lower() + ':' + str(data6)


def setCoin(argument1, argument2):
    with open("Index.json", "r") as file:
        data = json.load(file)
    if argument1.lower() in data:
        with open("coins.json", "r") as file:
            data2 = json.load(file)

        data6 = int(argument2)
        data7 = data.index(argument1.lower())
        data2.insert(data7, {argument1.lower(): {'Coins': data6}})
        index_data = data.index(argument1.lower())
        result = index_data + 1

        data2.remove(data2[result])
        with open("coins.json", "w") as file:
            json.dump(data2, file)
        with open("backup-coins.json", "w") as file:
            json.dump(data2, file)
        print(argument1.lower() + ':' + str(data6))
        return argument1.lower() + ':' + str(data6)

def reset():
    reset = []
    print("full reset!")
    with open("coins.json", "w") as file:
        json.dump(reset, file)
    with open("Index.json", "w") as file:
        json.dump(reset, file)
    with open("messages.json", "w") as file:
        json.dump(reset, file)
    with open("messages_index", "w") as file:
        json.dump(reset, file)

    return "completed"


def getCoinAmount(username):
    with open("coins.json", "r") as file:
        data = json.load(file)
    with open("Index.json", "r") as file:
        index = json.load(file)

    index = index.index(username.lower())
    data = data[index][username.lower()]["Coins"]
    return data
