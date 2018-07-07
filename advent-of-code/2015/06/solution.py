#!/usr/bin/python

with open('input.txt', 'r') as f:
	lights = []
	for i in range(1000):
		lights.append([])
		for j in range(1000):
			lights[i].append(False)
	for line in f:
		instructions = line.split()
		if instructions[0] == 'toggle':
			x1,y1 = (int(x) for x in instructions[1].split(','))
			x2,y2 = (int(x) for x in instructions[3].split(','))
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					lights[x][y] = not lights[x][y]
		elif instructions[1] == 'on':
			x1,y1 = (int(x) for x in instructions[2].split(','))
			x2,y2 = (int(x) for x in instructions[4].split(','))
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					lights[x][y] = True
		else:
			x1,y1 = (int(x) for x in instructions[2].split(','))
			x2,y2 = (int(x) for x in instructions[4].split(','))
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					lights[x][y] = False
	count = 0
	for i in range(1000):
		for j in range(1000):
			if lights[i][j]:
				count = count + 1
	print count
