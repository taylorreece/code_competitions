#!/usr/bin/env python3

counter = 0

with open('input.txt', 'r') as infile:
	for line in infile.readlines():
		counter += int(line.replace('+', ''))

print(counter)
