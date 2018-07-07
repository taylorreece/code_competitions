#!/usr/bin/python3

import itertools, re

def solve(N):
	if N == 0:
		return 'INSOMNIA'
	count = 0
	nums = set()
	i = 1
	while(len(nums) < 10):
		newnum = str(i*N)
		nums = set(list(nums) + list(newnum))	
		i = i + 1	
	return (i-1)*N

with open('input.txt', 'r') as f:
	num_problems = int(f.readline())
	for i in range(num_problems):
		print('Case #%s: %s' % (i+1, solve(int(f.readline()))))
