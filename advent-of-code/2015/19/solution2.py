#!/usr/bin/python3

rules = list()
target = ''

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

rules.sort(key = lambda x: len(x[1]), reverse=True)

count = 0
node = 0
while target != 'e':
	if target.find(rules[node][1]) != -1:
		target = target.replace(rules[node][1],rules[node][0],1)
		node = 0
		count = count + 1
	else:
		node = node + 1
print(count)
