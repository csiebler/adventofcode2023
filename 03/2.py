import os
import re
import numpy as np

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

# convert data to numpy array
data = np.array([list(line) for line in data.split('\n')])
print(data)

# generate data_mask, that is 1 if there is a digit, else 0
data_mask = np.where(np.char.isdigit(data), 1, 0)

# pad it by 1, so we can check the bordering elements easier
data_mask = np.pad(data_mask, 1, 'constant')

def get_multiplied_gears(y, x):
    # get relevant rows, but check we don't go out of bounds
    lines = []
    for i in range(-1, 2):
        if y+i > 0 or y+i < len(data):
            lines.append(''.join(data[y+i]))
                
    # use regex to extract all numbers from line and save them as triples (number, position, length)
    gear_numbers = []
    for line in lines:
        numbers = [(m.group(), m.start(), len(m.group())) for m in re.finditer(r'\d+', line)]
        for n in numbers:
            number, position, length = n
            x_start = position
            x_end = position + length - 1
            if (x_start <= x <= x_end) or (x_start == x + 1) or (x_end == x - 1):
                gear_numbers.append(int(number))
    assert(len(gear_numbers) == 2)
    return gear_numbers[0] * gear_numbers[1]

total = 0
# get all gear positions, that is where there is a * in data (y, x)
for gear in np.argwhere(data == '*'):
    y, x = gear
    
    # get 3x3 sub array around the gear's position
    subarray = data_mask[y:y+3, x:x+3]

    # now check if there are exactly two numbers bordering the gear
    numbers = 0
    
    # check top row
    if sum(subarray[0]) == 1 or sum(subarray[0]) == 3:
        numbers += 1
    elif sum(subarray[0]) == 2 and subarray[0][1] == 0:
        numbers += 2
    elif sum(subarray[0]) == 2:
        numbers += 1
    
    # middle row
    numbers += sum(subarray[1])
    
    # bottom row
    if sum(subarray[2]) == 1 or sum(subarray[2]) == 3:
        numbers += 1
    elif sum(subarray[2]) == 2 and subarray[2][1] == 0:
        numbers += 2
    elif sum(subarray[2]) == 2:
        numbers += 1
    
    # if we have exactly two numbers, multiply them and add to total
    if (numbers == 2):
        total += get_multiplied_gears(y,x)

print(total)