import os
import re

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

def rate_hand(hand):
    rating = 1
    
    # count each card in hand and put into array as tuples
    counts = sorted([(x, hand.count(x)) for x in set(hand)], key=lambda x: x[1], reverse=True)
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
    
    print(f"Hand {hand} --> {counts} --> {hand_mapping} --> {rating}")
    return rating

def convert_card(x):
    if x == 'T':
        return 10
    elif x == 'J':
        return 11
    elif x == 'Q':
        return 12
    elif x == 'K':
        return 13
    elif x == 'A':
        return 14
    else:
        return int(x)

hands = []
for line in data.split('\n'):
    hand, bid = line.split(' ')
    hand = [convert_card(x) for x in hand]
    normalized = ''.join(["{:02d}".format(x) for x in hand])
    rating = rate_hand(hand)
    hands.append({'hand': hand, 'normalized': normalized, 'bid': int(bid), 'rating': rating})

print(hands)

# now that we have all hands and rating, we need to sort by ratings
# if two cards have the same rating, we need to check char by char, which one is higher, and once we find a higher one, that hand wins

sorted_hands = sorted(hands, key=lambda x: (x['rating'], x['normalized']), reverse=True)

total = 0
for idx, hand in enumerate(sorted_hands):
    total += (len(hands) - idx) * hand['bid']

print(total)