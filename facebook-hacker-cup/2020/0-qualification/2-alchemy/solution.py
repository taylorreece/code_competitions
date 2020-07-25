#!/usr/bin/env python3

file_out = open('output.txt', 'w')

def output(line):
    print(line)
    file_out.write(f"{line}\n")

def solve(line):
    if (len(line) - 2 * line.count('A')) in [-1, 1]:
        return 'Y'
    return 'N'

with open('input.txt', 'r') as f:
    for i in range(int(f.readline())):
        f.readline()
        output(f"Case #{i+1}: {solve(f.readline().strip())}")