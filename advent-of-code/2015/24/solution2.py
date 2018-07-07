#!/usr/bin/python3

import itertools
from operator import mul
from functools import reduce

numbers = list()

with open('input.txt', 'r') as f:
	for line in f:
		numbers.append(int(line))

num_per_group = sum(numbers) / 4

# =============================================
def remainder_splitable(c,n, goal):
	if sum(c) == goal:
		return True
	r = set(n) - set(c)
	for i in range(1,len(r)):
		for comb in itertools.combinations(numbers,i):
			if sum(comb) == goal and remainder_splitable(c+comb, n, goal):
				return True
	return False

# =============================================

success_found = False
best_qe = 100000000000000
for i in range(1,len(numbers)):
	candidates = list()
	for comb in itertools.combinations(numbers,i):
		if sum(comb) == num_per_group:
			if remainder_splitable(comb, numbers, num_per_group):
				candidates.append(comb)
	if len(candidates):
		for c in candidates:
			qe = reduce(mul,c)
			best_qe = min(qe, best_qe)
		break
print(best_qe)
