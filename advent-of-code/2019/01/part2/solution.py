#!/usr/bin/env python3

my_sum = 0

def solve(mass):
    ret = 0
    while mass > 0:
        mass = int(mass/3) - 2
        if mass > 0:
            ret += mass
    return ret

with open('input.txt', 'r') as infile:
    for mass in infile.readlines():
        my_sum += solve(int(mass))

print(f"Sum: {my_sum}")