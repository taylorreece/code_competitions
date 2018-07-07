#!/usr/bin/python

count = 0
with open('input.txt') as f:
	for line in f:
		sides = [float(x) for x in line.split()]
		if 2*max(sides) < sum(sides):
			count += 1
print(count)
