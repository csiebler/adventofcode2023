import os
import re

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()
    
data = data.split('\n')
print(data)

# initialize new list of lists with same dimensions as data
marked = []
marked = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

def print_marked():
    print("--------")
    for line in marked:
        print(line)

def follow_and_mark(x, y, dx, dy):
    print(f"Following from {x}, {y} with {dx}, {dy}")
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
        
follow_and_mark(0, 0, 1, 0)

print_marked()
# count all fields that are not 0
total = sum([1 for line in marked for field in line if field != 0])
print(f"Total marked fields: {total}")