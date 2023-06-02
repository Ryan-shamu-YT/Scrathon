import json

def getInfo(key, json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    c = 0
    for i in data:
        if list(data[c])[0] == key:
            return str(data[c][key])
        c = c + 1
    return str(404)
