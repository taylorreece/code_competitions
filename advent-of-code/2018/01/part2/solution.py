#!/usr/bin/env python3
import sys 

frequencies_encountered = [0]

with open('input.txt', 'r') as infile:
	frequency_diffs = [int(line.replace('+', '')) for line in infile.readlines()]

idx = 0

while True:
	newval = frequencies_encountered[-1] + frequency_diffs[idx] 
	if newval in frequencies_encountered:
		print(newval)
		sys.exit()
	frequencies_encountered.append(newval)
	idx += 1
	if idx == len(frequency_diffs):
		idx = 0

