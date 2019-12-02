#!/usr/bin/env python3

my_sum = 0

def solve(mass):
    return int(mass/3) - 2

with open('input.txt', 'r') as infile:
    for mass in infile.readlines():
        my_sum += solve(int(mass))

print(f"Sum: {my_sum}")