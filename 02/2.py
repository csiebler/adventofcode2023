import os
import re

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

games = []
for line in data.splitlines():
    game = {
        "red": 0,
        "green": 0,
        "blue": 0        
    }
    content = line.split(":")[1]
    
    # get numbers and colors from each draw
    draws = content.split(";")
    for draw in draws:
        matches = re.findall(r"(\d+) (\w+)", draw)
        for match in matches:
            color = match[1]
            count = int(match[0])
            game[color] = max(count, game[color])

    games.append(game)

power = sum([game["red"] * game["green"] * game["blue"] for game in games])
print("Power:", power)