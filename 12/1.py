import os
import re

# Brute force solution :(

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

def is_valid(spring, blocks):
    # print(f"Checking if {spring} is matching {blocks}")
    lengths = [len(x) for x in spring.split('.') if x != '']
    return lengths == blocks

valid_combinations = 0

for line in data.split('\n'):
    springs, blocks = line.split(' ')
    blocks = [int(x) for x in blocks.split(',')]
    # remove unnecessary dots
    springs = re.sub(r'\.+', '.', springs.strip('.'))
    print(f"Springs: {springs} --> blocks: {blocks}")
    
    # count ? in springs
    unknowns = springs.count('?')
    
    # get all binary combinations for unknowns
    combinations = []
    for i in range(2**unknowns):
        combo = bin(i)[2:].zfill(unknowns).replace('0', '.').replace('1', '#')
        combinations.append(combo)
    
    for combination in combinations:
        # make copy of strings and replace ? with combinations
        springs_replaced = str(springs)
        for i in range(unknowns):
            springs_replaced = springs_replaced.replace('?', combination[i], 1)
        
        # check if valid
        if is_valid(springs_replaced, blocks):
            valid_combinations += 1

print(f"Valid combinations: {valid_combinations}")