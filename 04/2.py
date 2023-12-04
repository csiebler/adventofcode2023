import os
import re
import numpy as np

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

cards = []

# go through each card
for card in data.split("\n"):
    winning_numbers, drawn_numbers = [x.strip() for x in card.split(":")[1].split("|")]
    pattern = re.compile(r'\d+')
    
    winning_numbers = [int(x) for x in pattern.findall(winning_numbers)]
    drawn_numbers = [int(x) for x in pattern.findall(drawn_numbers)]
    wins = sum([1 for x in drawn_numbers if x in winning_numbers])
    
    cards.append({
        "id": card.split(":")[0].strip(),
        "wins": wins,
        "copies": 1,
    })

for i in range(len(cards)):
    current_card = cards[i]
    wins = current_card["wins"]
    print(f"Current card: {current_card} has {wins} wins")
    for j in range(wins):
        print(f"Adding {current_card['copies']} copies of {cards[i+j+1]}")
        cards[i+j+1]["copies"] += (current_card["copies"])
        print(f"Card {cards[i+j+1]} now has {cards[i+j+1]['copies']} copies")

num_cards = sum([x["copies"] for x in cards])
print(f"Total number of cards: {num_cards}")