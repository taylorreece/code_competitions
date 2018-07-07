#!/usr/bin/python

def decrypt(line):
	room = line.split('-')
	letters = '-'.join(room[:-1])
	shift = int(room[-1].split('[')[0])
	ret = ' '
	for letter in letters:
		if letter == '-':
			ret += ' '
		else:
			ret += chr((ord(letter)-97+shift) % 26 + 97)
	if 'north' in ret:
		print(letters, ret, shift)
	
with open('input.txt') as f:
	for line in f:
		decrypt(line)

