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

current_position = 'AAA'
target_position = 'ZZZ'
steps = 0

while True:
    instruction = instructions[steps % len(instructions)]
    if instruction == 'L':
        current_position = routings[current_position][0]
    else:
        current_position = routings[current_position][1]
    steps += 1
    if current_position == target_position:
        print(f"Reached goal after {steps} steps")
        break