#!/usr/bin/env python3

with open('input.txt', 'r') as infile:
    ints = [int(x) for x in infile.read().strip().split(',')]

idx = 0
ints[1] = 12
ints[2] = 2
while ints[idx] != 99:
    if ints[idx] == 1:
        ints[ints[idx+3]] = ints[ints[idx+1]] + ints[ints[idx+2]]
    elif ints[idx] == 2:
        ints[ints[idx+3]] = ints[ints[idx+1]] * ints[ints[idx+2]]
    idx += 4
print(ints[0])