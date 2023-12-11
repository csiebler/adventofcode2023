import os
import re
import math

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

galaxy = [list(line.strip()) for line in data.splitlines()]

def print_galaxy(g):
    for line in g:
        print(''.join(line))

expanded_galaxy = []

for line in galaxy:
    expanded_galaxy.append(line)
    if set(line) == set('.'):
        # append a copy of line, do not reference the same
        expanded_galaxy.append(line.copy())


empty_cols = []
for x in range(0, len(expanded_galaxy[0])):
    col = set([expanded_galaxy[y][x] for y in range(0, len(expanded_galaxy))])
    if col == set('.'):
        empty_cols.append(x)

print(f"Empty cols: {empty_cols}")
for idx, x in enumerate(empty_cols):
    for y in range(0, len(expanded_galaxy)):
        
        # now insert at x+idx
        expanded_galaxy[y].insert(x+idx, '.')
        
        print(f"Inserting {y} at {x+idx}")

print_galaxy(expanded_galaxy)

# find all # in the galaxy
stars = []
for y, line in enumerate(expanded_galaxy):
    for x, c in enumerate(line):
        if c == '#':
            stars.append((y, x))

print(stars)

def star_distance(star1, star2):
    # Walk shortest distance from star1 to star2, but keep in mind that we have to walk on the grid
    steps = abs(star2[0] - star1[0])  + abs(star2[1] - star1[1])
    return steps

# Now get all possible pairs
total_distances = 0
for i, star1 in enumerate(stars):
    for star2 in stars[i+1:]:
        d = star_distance(star1, star2)
        total_distances += d
        print(f"Star {star1} --> {star2}: {d}")
        
print(f"Total distances: {total_distances}")