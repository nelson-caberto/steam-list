import json
import csv

with open('json.txt','r') as jsonFile:
    rgGames = json.load(jsonFile)

keys = []
for game in rgGames:
    for key in game:
        if key not in keys:
            keys.append(key)

with open('games.csv','w',newline='') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=keys)
    writer.writeheader()
    for game in rgGames:
        writer.writerow(game)