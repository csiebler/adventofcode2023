import os
import re
import numpy as np

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

data = data.split('\n')

time = int(data[0].split(':')[1].replace(' ', ''))
distance = int(data[1].split(':')[1].replace(' ', ''))

times_won = 0

for t in range(0, time + 1):
    if (distance < t * (time - t)):
        times_won += 1
    if (t % 1000000 == 0):
        print(f"Checked {t}/{time} options")

print(f"Won race {times_won} times")
