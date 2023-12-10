import os
import re

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

pipes = [list('.' + line.strip() + '.') for line in data.splitlines()]

# first find starting tile
for y, line in enumerate(pipes):
    for x, tile in enumerate(line):
        if tile == 'S':
            sy, sx = y, x
            break
print(f"Starting position: {sy}, {sx}")

# figure out the starting tile
starting_tile = 'F'
if pipes[sy-1][sx] in ['7', 'F', '|'] and pipes[sy+1][sx] in ['|', 'L', 'J']:
    starting_tile = '|'
elif pipes[sy][sx-1] in ['L', 'F', '-'] and pipes[sy][sx+1] in ['-', 'J', '7']:
    starting_tile = '-'
elif pipes[sy-1][sx] in ['|', 'F', '7'] and pipes[sy][sx+1] in ['-', 'J', '7']:
    starting_tile = 'L'
elif pipes[sy-1][sx] in ['|', 'F', '7'] and pipes[sy][sx-1] in ['-', 'L', 'F']:
    starting_tile = 'J'
elif pipes[sy+1][sx] in ['|', 'L', 'J'] and pipes[sy][sx-1] in ['-', 'L', 'F']:
    starting_tile = '7'

# starting position with actual tile
pipes[sy][sx] = starting_tile

# get starting direction
direction = 'down'
if starting_tile in ['-', 'L', 'F']:
    direction = 'left'
elif starting_tile in ['J', '7']:
    direction = 'right'

print(f"Starting tile {starting_tile} with direction {direction}")

steps = 0
cy, cx = sy, sx

while True:
    current_tile = pipes[cy][cx]
    if current_tile == '|' and direction == 'down':
        cy += 1
    if current_tile == '|' and direction == 'up':
        cy -= 1
    elif current_tile == '-' and direction == 'right':
        cx += 1
    elif current_tile == '-' and direction == 'left':
        cx -= 1
    elif current_tile == 'L' and direction == 'down':
        cx += 1
        direction = 'right'
    elif current_tile == 'L' and direction == 'left':
        cy -= 1
        direction = 'up'
    elif current_tile == 'J' and direction == 'down':
        cx -= 1
        direction = 'left'
    elif current_tile == 'J' and direction == 'right':
        cy -= 1
        direction = 'up'
    elif current_tile == '7' and direction == 'right':
        cy += 1
        direction = 'down'
    elif current_tile == '7' and direction == 'up':
        cx -= 1
        direction = 'left'
    elif current_tile == 'F' and direction == 'left':
        cy += 1
        direction = 'down'
    elif current_tile == 'F' and direction == 'up':
        cx += 1
        direction = 'right'
    
    print(f"New position: {cy}, {cx}")
    steps += 1
    if cy == sy and cx == sx:
        print(f"Found starting position again after {steps} steps")
        print(f"Furthest point away was {int(steps/2)} steps")
        break