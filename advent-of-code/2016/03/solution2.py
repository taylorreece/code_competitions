#!/usr/bin/python

count = 0
with open('input.txt') as f:
	lines = []
	for line in f:
		lines.append(line)
	for i in range(len(lines) / 3):
		line1 = [float(x) for x in lines[i*3].split()]
		line2 = [float(x) for x in lines[i*3+1].split()]
		line3 = [float(x) for x in lines[i*3+2].split()]
		for sides in zip(*(line1,line2,line3)):
			if 2*max(sides) < sum(sides):
				count += 1
print(count)
