#!/usr/bin/python

with open('input.txt', 'r') as f:
	for line in f:
		floor = 0
		position = 1
		for char in line:
			if char == '(':
				floor = floor + 1
			else:
				floor = floor - 1
			if floor == -1:
				print position
				break
			position = position + 1
