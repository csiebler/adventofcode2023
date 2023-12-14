import os
import re

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()
    data = data.replace('#', '1').replace('.', '0')
    
puzzles = [x.split('\n') for x in data.split('\n\n')]

def find_horizontal_folding_line(puzzle):
    # mirror on each position
    fitting_line = -1
    
    for mirror_position in range(0, len(puzzle)-1):
        sum = 0
        for j in range(0, min(mirror_position+1, len(puzzle)-mirror_position-1)):
            sum += puzzle[mirror_position-j] - puzzle[mirror_position+j+1]
        if sum == 0:
            fitting_line = mirror_position
            break
    
    return fitting_line + 1

total = 0
for p in puzzles:   
    # convert puzzle to numbers, since each line is a binary number
    p_int = [int(x, 2) for x in p]
    print(p_int)
    
    # transpose p
    p_int_t = [int(''.join(a[x] for a in p), 2) for x in range(0, len(p[0]))]
    
    print(p_int_t)
    
    v = find_horizontal_folding_line(p_int)
    h = find_horizontal_folding_line(p_int_t)
    print(f"v: {v}, h: {h}")
    total += 100*v + h

print(total)