#!/usr/bin/env python3

import pprint
import time

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

location = [6,5]
direction = 1
steps = 0
max_steps = 0

while grid[location[1]][location[0]] < 368078:
    moved = False
    if direction == 4:
        moved = True
        location[0] += 1
        if steps == max_steps:
            direction = 1
            steps = 0
        else:
            steps += 1
    if direction == 1 and not moved:
        moved = True
        location[1] -= 1
        if steps == max_steps:
            max_steps += 1
            direction = 2
            steps = 0
        else:
            steps += 1
    if direction == 2 and not moved:
        moved = True
        location[0] -= 1
        if steps == max_steps:
            direction = 3
            steps = 0
        else:
            steps += 1
    if direction == 3 and not moved:
        moved = True
        location[1] += 1
        if steps == max_steps:
            direction = 4
            steps = 0
            max_steps += 1
        else:
            steps += 1
    grid[location[1]][location[0]] = sum([
        grid[location[1]-1][location[0]-1],
        grid[location[1]-1][location[0]],
        grid[location[1]-1][location[0]+1],
        grid[location[1]][location[0]-1],
        grid[location[1]][location[0]+1],
        grid[location[1]+1][location[0]-1],
        grid[location[1]+1][location[0]],
        grid[location[1]+1][location[0]+1],
    ])
print(grid[location[1]][location[0]])
