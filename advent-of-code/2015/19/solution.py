#!/usr/bin/python3

rules = list()
target = ''
results = set()

def find_offsets(haystack, needle):
	"""
	Find the start of all (possibly-overlapping) instances of needle in haystack
	"""
	offs = -1
	while True:
		offs = haystack.find(needle, offs+1)
		if offs == -1:
			break
		else:
			yield offs

with open('input.txt', 'r') as f:
	for line in f:
		if '=>' in line:
			rules.append(line.rstrip().split(' => '))
		elif len(line) > 1:
			target = line.rstrip()
		else:
			pass

for rule in rules:
	for loc in find_offsets(target, rule[0]):
		results.add(target[0:loc] + rule[1] + target[loc+len(rule[0]):])

print(len(results))
