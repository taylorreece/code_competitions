#!/usr/bin/python

from collections import Counter

def d_cmp(a,b):
	if a[1] < b[1]:
		return -1
	if a[1] > b[1]:
		return 1
	if a[0] < b[0]:
		return 1
	return -1

def real_room(line):
	""" Returns the rooms sector ID, or 0 if it is a fake room """
	room = line.split('-')
	letters = ''.join(room[:-1])
	code = ''.join([x[0] for x in sorted(Counter(letters).most_common(), d_cmp, reverse=True)][:5])
	check = room[-1].split('[')[1][:-2]
	if code == check:
		return int(room[-1].split('[')[0])
	return 0
	
count = 0
with open('input.txt') as f:
	for line in f:
		count += real_room(line)

print(count)
