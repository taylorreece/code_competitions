#!/usr/bin/python

import re

count = 0
regex = r'\[[a-z]*\]'

def valid(line):
	hypernets = re.findall(regex, line)
	line = re.sub(regex, '--', line)
	for i in range(len(line)-3):
		if line[i] == line[i+2] and line[i] != line[i+1] and any(line[i+1]+line[i]+line[i+1] in x for x in hypernets):
			return True
	return False

with open('input.txt') as f:
	for line in f:
		if valid(line):
			count += 1

print(count)
