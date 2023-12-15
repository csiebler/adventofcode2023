import os
import re

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()
    
puzzle = [list(x) for x in data.split('\n')]

for y in range(1, len(puzzle)):
    for x in range(0, len(puzzle[y])):
        
        if puzzle[y][x] in ['.', '#']:
            continue
        else:
            d = 0
            while (y-d > 0) and puzzle[y-1-d][x] not in ['O', '#']:
                puzzle[y-d][x] = '.'
                puzzle[y-1-d][x] = 'O'
                d += 1

total = 0
for idx, row in enumerate(puzzle):
    # count O in row
    print(row.count('O'), len(puzzle) - idx)
    total += row.count('O') * (len(puzzle) - idx)
        
for row in puzzle:
    print(''.join(row))

print(total)