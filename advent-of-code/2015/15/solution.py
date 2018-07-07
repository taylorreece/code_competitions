#!/usr/bin/python3

import functools
import itertools
import numpy
import re

foods = list()

with open('input.txt', 'r') as f:
	count = 0
	for line in f:
		name, cap, dur, fla, tex, cal = re.match(r'(\w+): \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+)', line).groups()
		foods.append((int(cap), int(dur), int(fla), int(tex)))#, int(cal))
		count = count + 1

best_score = 0

permutations = set()
for perm in [list(itertools.permutations(i)) for i in itertools.combinations_with_replacement(range(101),len(foods)) if sum(i)==100]:
	for p in perm:
		permutations.add(p)

for p in permutations:
	food_scores = list()
	for i in range(len(foods)):
		food_scores.append(tuple(p[i] * foods[i][j] for j in range(4)))
	score = functools.reduce(lambda x,y: x*y, [max(0,i) for i in map(sum,zip(*food_scores))])
	if score > best_score:
		best_score = score
print(best_score)
