#!/usr/bin/python

import re
import time

def decompress(line):
	pointer = 0
	ret = 0
	if '(' not in line:
		return len(line)
	while pointer < len(line):
		if line[pointer] != '(':
			ret += 1
			pointer += 1
		else:
			pointer2 = pointer
			while line[pointer2] != ')':
				pointer2 += 1
			vals = re.match(r'([0-9]*)x([0-9]*)',line[pointer+1:pointer2])
			chars,repeats = int(vals.group(1)), int(vals.group(2))
			pointer = pointer2+1
			ret += decompress(line[pointer:pointer+chars])*repeats
			pointer += chars
	return ret

for line in open('input.txt'):
	result = decompress(line.strip())
	print(result)
