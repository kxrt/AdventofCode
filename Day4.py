import numpy as np
from copy import deepcopy

from numpy.core.fromnumeric import transpose

with open('Day4_input_cards.txt') as f:
    lines_cards = [line.rstrip() for line in f]

cards = np.array_split(np.genfromtxt(lines_cards), 100)

numbers_str = open('Day4_input_numbers.txt').read()

numbers = list(map(int, numbers_str.split(',')))

cards_counter = deepcopy(cards)

for x in range(len(cards_counter)):
    for y in range(len(cards_counter[x])):
        for z in range(len(cards_counter[x][y])):
            cards_counter[x][y][z] = 0

winning_card = []
winning_num = 0
winning_num_index = 0

def check_winning_set():
    for x in range(len(cards_counter)):
        for y in range(len(cards_counter[x])):
            if np.sum(cards_counter[x][y]) == 5:
                global winning_card 
                winning_card = cards[x]
                return True
    for i in range(len(cards_counter)):
        for j in range(len(cards_counter[i])):
            if np.sum(np.transpose(cards_counter[i])[j]) == 5:
                winning_set = np.transpose(cards_counter[i])[j]
                winning_card = np.transpose(cards_counter[i])
                return True

for i in range(len(numbers)):  
    if check_winning_set():
            winning_num = numbers[i - 1]
            winning_num_index = i
            break        
    for x in range(len(cards)):
        for y in range(len(cards[0])):
            for z in range(len(cards[0][0])):
                if numbers[i] == cards[x][y][z]:
                    cards_counter[x][y][z] = 1

for n in range(winning_num_index):
    for x in range(len(winning_card)):
        for y in range(len(winning_card[x])):
            if winning_card[x][y] == numbers[n]:
                winning_card[x][y] = 0

def total(arr):
    total = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            total = total + arr[x][y]
    return total

print(total(winning_card) * winning_num)

# Part 2

cards_counter_2 = deepcopy(cards)

for x in range(len(cards_counter)):
    for y in range(len(cards_counter[x])):
        for z in range(len(cards_counter[x][y])):
            cards_counter_2[x][y][z] = 0

print('test')