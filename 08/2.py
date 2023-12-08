import os
import re

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

data = data.splitlines()

# Extract turning instructions
instructions = data[0]

# Extract all routings
routings = {}
for r in [re.findall(r'\b[A-Z]{3}\b', x) for x in data[2:]]:
    routings[r[0]] = (r[1], r[2])
print(routings)

current_positions = [x for x in list(routings.keys()) if x[2] == 'A']

# Find the shortest route to a Z position for each A position
required_steps = []
for i in range(len(current_positions)):
    steps = 0
    while True:
        instruction = instructions[steps % len(instructions)]
        if instruction == 'L':
            current_positions[i] = routings[current_positions[i]][0]
        else:
            current_positions[i] = routings[current_positions[i]][1]
        steps += 1
        if (current_positions[i][2] == 'Z'):
            print(f"Reached goal after {steps} steps")
            required_steps.append(steps)
            break
        
# find common denominator for all numbers in required_steps
from math import lcm
print(lcm(*required_steps))