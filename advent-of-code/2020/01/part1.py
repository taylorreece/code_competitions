#!/usr/bin/env python3

numbers = []

with open('input.txt', 'r') as infile:
    for line in infile.readlines():
        if line:
            numbers.append(int(line))

numbers.sort()

while numbers[0] + numbers[-1] != 2020:
    if numbers [0] + numbers[-1] < 2020:
        numbers = numbers[1:]
    else:
        numbers = numbers[0:-1]

print(numbers[0])
print(numbers[-1])
print(numbers[0] * numbers[-1])

