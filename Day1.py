# Part 1

import numpy as np

arr = np.genfromtxt('Day1_input.txt')

def increasing(array): 
    result = 0
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            result += 1
    return result 

print(increasing(arr))

# Part 2

newarr = []

for x in range(0, len(arr) - 2):
    newarr.append(arr[x] + arr[x + 1] + arr[x + 2])

print(increasing(newarr))