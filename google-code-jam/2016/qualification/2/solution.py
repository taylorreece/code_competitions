#!/usr/bin/python3

import itertools, re

def solve(a):
	count = 0
	for i in range(len(a)-1):
		if a[i] != a[i+1]:
			count = count + 1
	return count

with open('input_large.txt', 'r') as f:
	num_problems = int(f.readline())
	for i in range(num_problems):
		a = list(f.readline().rstrip() + '+')
		print('Case #%s: %s' % (i+1, solve(a)))
