#!/usr/bin/python
import itertools

best_distance = 1000000000000000

distances = dict()
with open('input.txt', 'r') as f:
	for line in f:
		a,b = line.split(' = ')
		a1,a2 = a.split(' to ')
		try:
			distances[a1][a2] = int(b)
		except KeyError:
			distances[a1] = dict()
			distances[a1][a2] = int(b)
		try:
			distances[a2][a1] = int(b)
		except KeyError:
			distances[a2] = dict()
			distances[a2][a1] = int(b)

for perm in itertools.permutations(distances):
	distance = 0
	for i in range(len(perm)-1):
		distance = distance + distances[perm[i]][perm[i+1]]
	if distance < best_distance:
		best_distance = distance

print best_distance
