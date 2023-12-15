import os
import re

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

data = data.split(',')
print(data)

total = 0
for d in data:
    v = 0
    for c in d:
        v = ((v + ord(c)) * 17) % 256
    total += v
print(total)        