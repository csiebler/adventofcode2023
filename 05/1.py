import os
import re
import numpy as np

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

# remove empty lines from data
data = [line for line in data.split('\n') if line.strip() != '']

# get seeds from first line via regex
seeds = [int(x) for x in re.findall(r'\d+', data[0])]
print("Seeds:", seeds)

# Now get all maps, we don't really care what they are
maps = []
for line in data[1:]:
    if "map" in line:
        maps.append([])
    else:
        mapping = [int(x) for x in re.findall(r'\d+', line)]        
        maps[-1].append({
            "source": mapping[1],
            "destination": mapping[0],
            "range": mapping[2]
        })
        
print(maps)

outputs = []
outputs.append(seeds)

# now map all inputs through all the mapping tables
for map in maps:
    
    # the current input is the last output, just copy it so we can edit it
    outputs.append(outputs[-1])

    for i in range(0, len(outputs[-1])):
        current_value = outputs[-1][i]
    
        for mapping in map:
            print(f"Mapping {mapping['source']} to {mapping['destination']} with range {mapping['range']}")
            # check if number falls within the range of the current map
            if current_value >= mapping['source'] and current_value < (mapping['source'] + mapping['range']):
                delta = current_value - mapping['source']
                outputs[-1][i] = mapping['destination'] + delta
                print("Mapped", current_value, "to", outputs[-1][i])

    print(f"All values have been mapped to {outputs[-1]}")

print("Closest location:", min(outputs[-1]))