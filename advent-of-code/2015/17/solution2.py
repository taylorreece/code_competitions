#!/usr/bin/python3

import itertools

total_liters = 150

containers = list()
with open('input.txt', 'r') as f:
	for line in f:
		containers.append(int(line))	

num_perms = 0
stop = False
for i in range(len(containers)):
	if not stop:
		for perm in itertools.combinations(containers, i):
			if sum(perm) == total_liters: 
				stop = True
				num_perms = num_perms + 1
				print(perm)
print(num_perms)
