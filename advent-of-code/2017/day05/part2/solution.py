#!/usr/bin/env python3
import time
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
        prev_value = puzzle[index]
        if puzzle[index] >= 3:
            puzzle[index] -= 1
        else:
            puzzle[index] += 1
        index += prev_value
    return num_steps

puzzle = read_puzzle()
print(solve(puzzle))
