#!/usr/bin/python
import itertools, re

happiness = dict()
happiness['Taylor'] = dict()

best_h = -10000000000

with open('input.txt', 'r') as f:
	for line in f:
		p1, gainlose, h, p2 = re.match(r'([A-Za-z]+) would (....) ([0-9]+) happiness units by sitting next to ([A-Za-z]+)',line).groups()
		if gainlose == 'gain':
			h = int(h)
		else:
			h = -int(h)
		try:
			happiness[p1][p2] = h
		except KeyError:
			happiness[p1] = dict()
			happiness[p1][p2] = h
			happiness['Taylor'][p1] = 0
			happiness[p1]['Taylor'] = 0

for perm in itertools.permutations(happiness):
	h = happiness[perm[0]][perm[-1]] + happiness[perm[-1]][perm[0]]
	for i in range(len(perm)-1):
		h = h + happiness[perm[i]][perm[i+1]] + happiness[perm[i+1]][perm[i]]
	if h > best_h:
		best_h = h

print best_h
