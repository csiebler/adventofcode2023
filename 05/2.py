import os
import re
import numpy as np

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

# remove empty lines from data
data = [line for line in data.split('\n') if line.strip() != '']

# get seeds as tuples from first line via regex
seeds_raw = [int(x) for x in re.findall(r'\d+', data[0])]

seeds = []
for i in range(0, len(seeds_raw), 2):
    # ranges are inclusive
    seeds.append({"range_start": seeds_raw[i], "range_end": seeds_raw[i] + seeds_raw[i+1] - 1})

# sort seeds by range start
seeds = sorted(seeds, key=lambda x: x['range_start'])

print("Seed ranges:", seeds)

# Now get all maps, we don't really care what they are
maps = []
for line in data[1:]:
    if "map" in line:
        maps.append([])
    else:
        mapping = [int(x) for x in re.findall(r'\d+', line)]
        maps[-1].append({
            "range_start": mapping[1],
            "range_end": mapping[1] + mapping[2] - 1,
            "shift_by": mapping[0] - mapping[1]
        })
        
# now sort the maps by source start
for i in range(0, len(maps)):
    maps[i] = sorted(maps[i], key=lambda x: x['range_start'])

def print_mappings(mappings):
    for m in mappings:
        print(f"{m['range_start']} -> {m['range_end']} with shift_by {m['shift_by']}")
        
for stage in maps:
    print("New stage with following mappings")
    print_mappings(stage)
        

def propagate_ranges(input_ranges, mappings):
    propagated_ranges = []
    
    print("--------------------------")
    print(f"Will now map input ranges {input_ranges}")
    print_mappings(mappings)
    
    for input_range in input_ranges:      
        current_range = input_range
        print(f"--> Working on range {current_range}")
        
        l = len(propagated_ranges)
        was_range_mapped = False
        for mapping in mappings:
            # check if mapping is relevant
            if (mapping['range_end'] < current_range['range_start']):
                print(f"Mapping is too small, skipping...")
                # continue
            elif (mapping['range_start'] > current_range['range_end']):
                print(f"Mapping is too big, skipping...")
                # continue
            else:
                print(f"Mapping is relevant, mapping {current_range} via {mapping}")
                # cut off front if mapping starts within the range
                if (mapping['range_start'] > current_range['range_start']):
                    print(f"Cutting off the beginning")
                    propagated_ranges.append({
                        "range_start": current_range['range_start'],
                        "range_end": mapping['range_start'] - 1
                    })
                    current_range['range_start'] = mapping['range_start']
                
                if mapping['range_start'] <= current_range['range_start'] and current_range['range_end'] <= mapping['range_end']:
                    propagated_ranges.append({
                        "range_start": current_range['range_start'] + mapping['shift_by'],
                        "range_end": current_range['range_end'] + mapping['shift_by']
                    })
                    current_range['range_start'] = current_range['range_end'] + 1
                    break
                elif mapping['range_start'] <= current_range['range_start'] and current_range['range_end'] > mapping['range_end']:
                    propagated_ranges.append({
                        "range_start": current_range['range_start'] + mapping['shift_by'],
                        "range_end": mapping['range_end'] + mapping['shift_by']
                    })

                # cut end off if needed but make sure it is still processed by other mappings
                if (mapping['range_end'] < current_range['range_end']):
                    print(f"Cutting off the end")
                    current_range['range_start'] =  mapping['range_end'] + 1
                
                was_range_mapped = True

        if (not was_range_mapped):
            print(f"Range {current_range} wasn't mapped, adding it as is")
            propagated_ranges.append(current_range)
            
    # we need to sort ranges before we return it
    propagated_ranges = sorted(propagated_ranges, key=lambda x: x['range_start'])
    
    print(f"Mapped input_ranges to {propagated_ranges}")
    return propagated_ranges

outputs = []
outputs.append(seeds)

# now map all inputs through all the mapping tables
for m in maps:
       
    # map all seed ranges to their destination(s), the number of seed maps might increase
    propagated_ranges = propagate_ranges(outputs[-1], m)
    outputs.append(propagated_ranges)
    
print("Closest location:", min([x['range_start'] for x in outputs[-1]]))