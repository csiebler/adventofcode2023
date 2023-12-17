import os
import re

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()
    
data = data.split('\n')

marked = []
marked = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

def print_marked():
    print("--------")
    for line in marked:
        print(line)

def follow_and_mark(x, y, dx, dy):
    while (x >= 0 and x < len(data[0])) and (y >= 0 and y < len(data)):
        # encode in binary all 4 directions
        # 1 = right, 2 = down, 4 = left, 8 = up
        # check if bits 1,2,3,4 are already marked
        if marked[y][x] & 1 and dx == 1:
            break
        elif marked[y][x] & 2 and dy == 1:
            break
        elif marked[y][x] & 4 and dx == -1:
            break
        elif marked[y][x] & 8 and dy == -1:
            break
        
        if dx == 1:
            marked[y][x] |= 1
        if dy == 1:
            marked[y][x] |= 2
        if dx == -1:
            marked[y][x] |= 4
        if dy == -1:
            marked[y][x] |= 8
        
        if data[y][x] == '-' and abs(dy) == 1:
            dx, dy = -1, 0
            # fork off a new beam
            follow_and_mark(x+1, y, 1, 0)
        elif data[y][x] == '|' and abs(dx) == 1:
            dx, dy = 0, -1
            # fork off a new beam
            follow_and_mark(x, y+1, 0, 1)
        elif (data[y][x] == '/' and dx == 1) or (data[y][x] == '\\' and dx == -1):
            dx, dy = 0, -1
        elif (data[y][x] == '/' and dx == -1) or (data[y][x] == '\\' and dx == 1):
            dx, dy = 0, 1
        elif (data[y][x] == '/' and dy == 1) or (data[y][x] == '\\' and dy == -1):
            dx, dy = -1, 0
        elif (data[y][x] == '/' and dy == -1) or (data[y][x] == '\\' and dy == 1):
            dx, dy = 1, 0
            
        x += dx
        y += dy
        
# Part 2, messy code with global variable but let's just get it done

def test_run(x, y, dx, dy):
    global marked
    marked = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
    follow_and_mark(x, y, dx, dy)
    v = sum([1 for line in marked for field in line if field != 0])
    if v == 0:
        print(f"v = 0 for {x}, {y}, {dx}, {dy}")
    return v

total = 0
for x in range (0, len(data[0])):  
    total = max(total, test_run(x, 0, 0, 1))
    total = max(total, test_run(x, len(data)-1, 0, -1))
    
for y in range (0, len(data)):
    total = max(total, test_run(0, y, 1, 0))
    total = max(total, test_run(len(data[0])-1, y, -1, 0))
    
print(f"Total best score: {total}")

