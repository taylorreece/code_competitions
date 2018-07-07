#!/usr/bin/python
import re

total = 0

with open('input.txt') as f:
	for line in f:
		total = total + sum([int(x) for x in re.findall(r'-?[0-9]+',line)])

print total	
