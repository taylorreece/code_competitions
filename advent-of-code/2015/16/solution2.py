#!/usr/bin/python3
import re
desired = {
	'children': '==3',
	'cats': '>7',
	'samoyeds': '==2',
	'pomeranians': '<3',
	'akitas': '==0',
	'vizslas': '==0',
	'goldfish': '<5',
	'trees': '>3',
	'cars': '==2',
	'perfumes': '==1'
}
aunts = dict()
with open('input.txt','r') as f:
	for line in f:
		num, objects = line.split(': ', 1)
		objects = {a : int(b) for a,b in re.findall(r'([a-z]+): (\d+)',objects)}
		aunts[num] = objects

for aunt, objects in aunts.items():
	success = True
	for o in objects:
		check = '%s%s' % (objects[o],desired[o])
		if not eval(check):
			success = False
	if success:
		print(aunt)
