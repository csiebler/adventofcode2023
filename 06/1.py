import os
import re
import numpy as np

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

data = data.split('\n')

times = [int(x) for x in re.findall(r'\d+', data[0])]
distances = [int(x) for x in re.findall(r'\d+', data[1])]

races = [{'time': times[i], 'best_distance': distances[i]} for i in range(len(times))]

speed_gain_per_ms = 1
total_options = 1

for race in races:
    times_won = 0
    
    # go through all different options for holding button down
    for t in range(0, race['time'] + 1):
        speed = speed_gain_per_ms * t
        remaining_time_after_charge = race['time'] - t
        distance_travelled = speed * remaining_time_after_charge
        
        if (distance_travelled > race['best_distance']):
            times_won += 1
        
        print(f"Race: {race} - Option: {t} - Speed: {speed} - Distance: {distance_travelled}")
    
    print(f"Won race {race} exactly {times_won} times")
    total_options *= times_won
    
print(f"Total options: {total_options}")