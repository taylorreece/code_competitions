#!/usr/bin/python

commands = list()

with open('input.txt','r') as f:
	for line in f:
		commands.append(line.rstrip())	

a = 1
b = 0
loc = 0

while True :
	command, args = commands[loc].split(' ', 1)
	jumped = False
	if command == 'hlf':
		if args=='a':
			a = int(a / 2)
		else:
			b = int(b / 2)
	elif command == 'tpl':
		if args == 'a':
			a = a * 3
		else:
			b = b * 3
	elif command == 'jmp':
		loc = loc + int(args)
		jumped = True
	elif command == 'inc':
		if args == 'a':
			a = a + 1
		else:
			b = b + 1
	elif command == 'jie':
		x,y = args.split(', ')
		if x == 'a' and a % 2 == 0:
			loc = loc + int(y)
			jumped = True
		elif x == 'b' and b % 2 == 0:
			loc = loc + int(y)
			jumped = True
	elif command == 'jio':
		x,y = args.split(', ')
		if x == 'a' and a == 1:
			loc = loc + int(y)
			jumped = True
		elif x == 'b' and b == 1:
			loc = loc + int(y)
			jumped = True
	if not jumped:
		loc = loc + 1
	if loc >= len(commands):
		break
print(b)
