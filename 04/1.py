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
    
    score = wins
    if wins > 1:
        score = 2 ** (wins-1) 
    
    cards.append({
        "id": card.split(":")[0].strip(),
        "wins": wins,
        "score": score
    })

# now calculate total score
total_score = sum([x["score"] for x in cards])
print(f"Total score: {total_score}")
