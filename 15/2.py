import os

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    data = f.read()

data = data.split(',')

def hash_label(s):
    v = 0
    for c in s:
        v = ((v + ord(c)) * 17) % 256
    return v

boxes = {}

for d in data:
    operator = '-'
    if '=' in d: 
        label, focal_length = d.split('=')
        box_id = int(hash_label(label))
        focal_length = int(focal_length)
        if box_id not in boxes:
            boxes[box_id] = {label: focal_length}
        else:
            boxes[box_id][label] = focal_length
    else:
        label = d.split('-')[0]
        box_id = int(hash_label(label))
        if box_id in boxes and label in boxes[box_id]:
            boxes[box_id].pop(label)

total = 0
for box_id, lenses in boxes.items():
    print(f"box: {box_id}, lenses: {lenses}")
    for idx, (label, focal_length) in enumerate(lenses.items()):
        total += (box_id + 1) * (idx+1) * focal_length
print(total)