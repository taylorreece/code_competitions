#!/usr/bin/python
import re
with open('input.txt', 'r') as f:
	total_chars = 0
	total_encoded_chars = 0
	for line in f:
		line = line.strip('\n')
		total_chars = total_chars + len(line)
		total_encoded_chars = total_encoded_chars + len(re.escape(line))+2
	print total_encoded_chars - total_chars
