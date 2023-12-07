import os
import re

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

def rate_hand(hand):
    rating = 1
    
    # count each card in hand and put into array as tuples
    counts = sorted([(x, hand.count(x)) for x in set(hand)], key=lambda x: x[1], reverse=True)
    
    num_jokers = hand.count(1)
    
    # Remove joker from counts & use as most dominant card
    # Only do this if not everything is a joker (5 jokers win anyway)
    if num_jokers < 5:
        counts = [x for x in counts if x[0] != 1]
        counts[0] = (counts[0][0], counts[0][1] + num_jokers)
    
    hand_mapping = int(''.join([str(x[1]) for x in counts]))
       
    if hand_mapping == 5:
        rating = 7
    elif hand_mapping == 41:
        rating = 6
    elif hand_mapping == 32:
        rating = 5
    elif hand_mapping == 311:
        rating = 4
    elif hand_mapping == 221:
        rating = 3
    elif hand_mapping == 2111:
        rating = 2
           
    print(f"Hand {hand} --> Jokers {num_jokers} --> {counts} --> {hand_mapping} --> {rating}")
    return rating

def convert_card(x):
    card_values = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
    return card_values.get(x) if x in card_values else int(x)

hands = []
for line in data.split('\n'):
    hand, bid = line.split(' ')
    hand = [convert_card(x) for x in hand]
    normalized = ''.join(["{:02d}".format(x) for x in hand])
    rating = rate_hand(hand)
    hands.append({'hand': hand, 'normalized': normalized, 'bid': int(bid), 'rating': rating})

print(hands)

# This all stays the same
sorted_hands = sorted(hands, key=lambda x: (x['rating'], x['normalized']), reverse=True)

total = 0
for idx, hand in enumerate(sorted_hands):
    total += (len(hands) - idx) * hand['bid']

print(total)