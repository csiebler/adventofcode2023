import os
import re

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    code = f.read()

total = 0
for line in code.split("\n"):    
    # remove any non digits from line
    line = re.sub(r'\D', '', line)
    total += int(line[0] + line[-1])
    
print(total)