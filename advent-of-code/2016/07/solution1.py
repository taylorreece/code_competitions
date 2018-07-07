#!/usr/bin/python

import re

count = 0

reverse_pair = lambda pair: pair[0] == pair[3] and pair[1] == pair[2] and pair[0] != pair[1]

def valid(line):
	for substr in re.findall(r'\[[a-z]*\]', line):
		for i in range(len(substr)-4):
			if reverse_pair(substr[i:i+4]):
				return False
	for i in range(len(line)-4):
		if reverse_pair(line[i:i+4]):
			return True

with open('input.txt') as f:
	for line in f:
		if valid(line):
			count += 1

print(count)
