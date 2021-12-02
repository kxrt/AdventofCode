# Part 1

import numpy as np

with open('Day2_input.txt') as f:
    lines = [line.rstrip() for line in f]

position = [0, 0]

for x in range(len(lines)):
    num = int(lines[x][len(lines[x]) - 1]) # Last character of string
    if lines[x][0] == 'f':
        position[0] += num
    elif lines[x][0] == 'u':
        position[1] -= num
    else:
        position[1] += num

print(position[0] * position[1]) # Ans: 2073315

# Part 2

aim = 0

position_2 = [0, 0]

for x in range(len(lines)):
    num = int(lines[x][len(lines[x]) - 1]) # Last character of string
    if lines[x][0] == 'u':
        aim -= num
    elif lines[x][0] == 'd':
        aim += num
    else:
        position_2[0] += num
        position_2[1] += (aim * num)

print(position_2[0] * position_2[1]) # Ans: 1840311528