import os
import re
import math

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

galaxy = [list(line.strip()) for line in data.splitlines()]
warp = 1000000

def print_galaxy(g):
    for line in g:
        print(''.join(line))

empty_cols = []
for x in range(0, len(galaxy[0])):
    col = set([galaxy[y][x] for y in range(0, len(galaxy))])
    if col == set('.'):
        empty_cols.append(x)

empty_rows = []
for y in range(0, len(galaxy)):
    if set(galaxy[y]) == set('.'):
        empty_rows.append(y)

print_galaxy(galaxy)
print(f"Empty cols: {empty_cols}, Empty rows: {empty_rows}")

# find all # in the galaxy
stars = []
for y, line in enumerate(galaxy):
    for x, c in enumerate(line):
        if c == '#':
            stars.append((y, x))

print(stars)

def star_distance(star1, star2):   
    dist_y = abs(star2[0] - star1[0])
    dist_x = abs(star2[1] - star1[1])
    
    # get indexes rows between star1 and star2
    row_min = min(star1[0], star2[0]) + 1
    row_max = max(star1[0], star2[0])
    col_min = min(star1[1], star2[1]) + 1
    col_max = max(star1[1], star2[1])
    
    for i in empty_rows:
        if i in range(row_min, row_max):
            dist_y += (warp-1)
            
    for i in empty_cols:
        if i in range(col_min, col_max):
            dist_x += (warp-1)
    
    steps = dist_y + dist_x
    return steps

# Now get all possible pairs
total_distances = 0
for i, star1 in enumerate(stars):
    for star2 in stars[i+1:]:
        d = star_distance(star1, star2)
        total_distances += d
        
print(f"Total distances: {total_distances}")