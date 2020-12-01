#!/usr/bin/env python3

numbers = []

with open('input.txt', 'r') as infile:
    for line in infile.readlines():
        if line:
            numbers.append(int(line))

def solve(numbers, number):
    numbers.sort()
    while numbers[0] + numbers[-1] != 2020 - number and len(numbers) > 1:
        if numbers [0] + numbers[-1] < 2020 - number:
            numbers = numbers[1:]
        else:
            numbers = numbers[0:-1]
    if len(numbers) > 1:
        return numbers[0] * numbers[-1] * number
    else:
        return None

for i in range(len(numbers)):
    solution = solve(numbers[0:i] + numbers[i+1:], numbers[i])
    if solution:
        print(solution)
        break