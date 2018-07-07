#!/usr/bin/python

with open('input.txt', 'r') as f:
	total_chars = 0
	total_string_chars = 0
	for line in f:
		line = line.strip('\n')
		total_chars = total_chars + len(line)
		total_string_chars = total_string_chars + len(eval(line))
	print total_chars - total_string_chars
