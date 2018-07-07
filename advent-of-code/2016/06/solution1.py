#!/usr/bin/python

lines = []

with open('input.txt') as f:
	for line in f:
		lines.append(line.strip())

print(''.join([max(zip((x.count(item) for item in set(x)), set(x)))[1] for x in zip(*lines)]))
