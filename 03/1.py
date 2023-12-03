import os
import re
import scipy
import numpy as np

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

# convert data to numpy array
data = np.array([list(line) for line in data.split('\n')])

# generate mask that is 1 when data is not a dot and not a number
mask = np.where((data != '.') & (~np.char.isnumeric(data)), 1, 0)

# now convolve mask with a 3x3 kernel of ones
mask = scipy.signal.convolve2d(mask, np.ones((3, 3)), 'same')
mask = np.where(mask > 0, 1, 0)

# now check each line for numbers and overlay mask
total = 0
for y, data_y in enumerate(data):
    numbers = []
    line = ''.join(data_y)
    
    # use regex to extract all numbers from line and save them as triples (number, position, length)
    numbers = [(m.group(), m.start(), len(m.group())) for m in re.finditer(r'\d+', line)]    
    for n in numbers:
        number, position, length = n
        if sum([mask[y][x] for x in range(position, position+length)]) >= 1:
            total += int(number)

print(total)