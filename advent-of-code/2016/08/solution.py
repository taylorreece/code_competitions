#!/usr/bin/python

import re

width = 50
height = 6

class Screen(object):
	def __init__(self):
		self.map = [[False]*width for x in range(height)]

	def rect(self, x, y):
		for i in range(y):
			for j in range(x):
				self.map[i][j] = True

	def rotate(self, thing, index, places):
		if thing == 'column':
			line = [x[index] for x in self.map]
			line = line[-places:] + line[:-places]
			for y in range(height):
				self.map[y][index] = line[y]
		if thing == 'row':
			line = self.map[index]
			self.map[index] = line[-places:] + line[:-places]
			
	def __str__(self):
		ret = ''
		for line in self.map:
			for c in line:
				if c: ret += '#'
				else: ret += '.'
			ret += '\n'
		return ret

	def count_on(self):
		return [y for x in self.map for y in x].count(True)

s = Screen()
with open('input.txt') as f:
	for line in f:
		if 'rect' == line[:4]:
			vals = re.match('rect ([0-9]*)x([0-9]*)',line)
			s.rect(int(vals.group(1)), int(vals.group(2)))
		if 'rotate' == line[:6]:
			vals = re.match('rotate ([a-z]*) [xy]=([0-9]*) by ([0-9]*)',line)
			s.rotate(vals.group(1), int(vals.group(2)), int(vals.group(3)))

print(s)			
print(s.count_on())
