#!/usr/bin/python

with open('input.txt', 'r') as f:
	total = 0
	for line in f:
		x,y = dict(), dict()
		x[0],y[0],x[1],y[1] = 0,0,0,0
		locations = dict()
		locations['0,0'] = 1
		count = 0
		for direction in line:
			if direction == '^':
				y[count % 2] = y[count % 2] + 1
			if direction == 'v':
				y[count % 2] = y[count % 2] - 1
			if direction == '>':
				x[count % 2] = x[count % 2] + 1
			if direction == '<':
				x[count % 2] = x[count % 2] - 1
			count = count + 1
			for i in (0,1):
				location = str(x[i]) + ',' + str(y[i])
				locations[location] = 1
		print len(locations)
