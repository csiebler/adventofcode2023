import os
import re

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

def predict_next_value(series):    
    deltas = [series[i+1] - series[i] for i in range(len(series) - 1)]
    print(f"Deltas: {deltas}")
    if (set(deltas) == {0}):
        return series[-1]
    else:
        return series[-1] + predict_next_value(deltas)

total = 0
for line in data.splitlines():
    # get all numbers from lines, numbers can also be negative    
    series = [int(x) for x in re.findall(r'-?\d+', line)]
    print(f"Predicting series:\n{' '.join([str(x) for x in series])}")
    total += predict_next_value(series)
    
print(f"Total sum of series: {total}")
