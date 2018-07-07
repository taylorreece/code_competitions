#!/usr/bin/env python3

def read_puzzle():
    puzzle = []
    with open('input.txt','r') as f:
        for line in f.readlines():
            puzzle.append(int(line))
    return puzzle

def solve(puzzle):
    index = 0
    num_steps = 0
    while 0 <= index and index < len(puzzle):
        num_steps += 1
        puzzle[index] += 1
        index += puzzle[index] - 1
    return num_steps

puzzle = read_puzzle()
print(solve(puzzle))
