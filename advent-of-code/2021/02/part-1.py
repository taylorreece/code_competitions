#!/usr/bin/env python3

depth = 0
position = 0

with open('input.txt', 'r') as infile:
  for line in infile:
    [direction, x] = line.split()
    if direction == "forward":
      position += int(x)
    elif direction == "up":
      depth -= int(x)
    else:
      depth += int(x)

print(depth*position)
