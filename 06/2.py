import os
import re

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

data = data.split('\n')

time = int(data[0].split(':')[1].replace(' ', ''))
distance = int(data[1].split(':')[1].replace(' ', ''))

# To win, we need to solve distance < t_charge * (time - t_charge)
sol1 = int(time/2 + ((-1 * time/2)**2 - distance) ** 0.5)
sol2 = int(time/2 - ((-1 * time/2)**2 - distance) ** 0.5)

# Winning count is the difference
print(f"Winning count is {abs(sol1 - sol2)}")

# Brute force solution

# times_won = 0
# for t in range(0, time + 1):
#     if (distance < t * (time - t)):
#         times_won += 1
#     if (t % 1000000 == 0):
#         print(f"Checked {t}/{time} options")

# print(f"Won race {times_won} times")
