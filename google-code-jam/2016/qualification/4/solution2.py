#!/usr/bin/python3

def solve(K,C,S):
	if S >= K:
		return ' '.join([str(i) for i in range(1,S+1)])
	else:
		return 'IMPOSSIBLE'

with open('input.txt', 'r') as f:
	num_problems = int(f.readline())
	for i in range(num_problems):
		K,C,S = [int(i) for i in f.readline().rstrip().split()]
		print('Case #%s: %s' % (i+1, solve(K,C,S)))
