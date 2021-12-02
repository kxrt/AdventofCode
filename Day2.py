# Part 1

import numpy as np

with open('Day2_input.txt') as f:
    lines = [line.rstrip() for line in f]

position = [0, 0]

for x in range(len(lines)):
    if lines[x][0] == 'f':
        position[0] = position[0] + int(lines[x][len(lines[x]) - 1])
    elif lines[x][0] == 'u':
        position[1] = position[1] - int(lines[x][len(lines[x]) - 1])
    else:
        position[1] = position[1] + int(lines[x][len(lines[x]) - 1])

print(position[0] * position[1]) # Ans: 2073315

# Part 2

aim = 0

position_2 = [0, 0]

for x in range(len(lines)):
    if lines[x][0] == 'u':
        aim = aim - int(lines[x][len(lines[x]) - 1])
    elif lines[x][0] == 'd':
        aim = aim + int(lines[x][len(lines[x]) - 1])
    else:
        position_2[0] = position_2[0] + int(lines[x][len(lines[x]) - 1])
        position_2[1] = position_2[1] + (aim * int(lines[x][len(lines[x]) - 1]))

print(position_2[0] * position_2[1]) # Ans: 1840311528