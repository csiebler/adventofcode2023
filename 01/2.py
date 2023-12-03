import os
import re

number_words = {
    "one": "o1ne",
    "two": "t2wo",
    "three": "t3hree",
    "four": "f4our",
    "five": "f5ive",
    "six": "s6ix",
    "seven": "s7even",
    "eight": "e8ight",
    "nine": "n9ine"
}

# load data.txt from current folder
with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as f:
    code = f.read()

total = 0
for line in code.split("\n"):
    
    for word, number in number_words.items():
        line = line.replace(word, number)
    
    line = re.sub(r'\D', '', line)
    total += int(line[0] + line[-1])
    
print("Total: ", total)