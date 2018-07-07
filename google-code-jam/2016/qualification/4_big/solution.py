#!/usr/bin/python3

import itertools, re

def expand(s,x,C,S):
	ret = ''
	if C == 1:
		return x
	else:
		for a in x:
			if a == 'G':
				ret = ret + 'G' * len(s)
			else:
				ret = ret + s
	ret = ret[:S]
	return expand(s,ret,C-1,S)

def solve(K,C,S):
	starters = [''.join(i) for i in itertools.product('GL', repeat=K)]
	enders = []
	for s in starters:
		enders.append(list(expand(s,s,C,S)))
	instances = list(zip(*enders[:-1]))
	instances = [len(set(i)) for i in instances]
	return instances

with open('input.txt', 'r') as f:
	num_problems = int(f.readline())
	for i in range(num_problems):
		K,C,S = [int(i) for i in f.readline().rstrip().split()]
		print('Case #%s: %s' % (i+1, solve(K,C,S)))
