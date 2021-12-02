#!/usr/bin/env python3

depth = 0
position = 0
aim = 0

with open('input.txt', 'r') as infile:
  for line in infile:
    [direction, x] = line.split()
    if direction == "forward":
      position += int(x)
      depth += aim * int(x)
    elif direction == "up":
      aim -= int(x)
    else:
      aim += int(x)

print(depth*position)
