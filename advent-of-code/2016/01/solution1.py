#!/usr/bin/python

class Santa:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.d = 0 # North... East is 1, south is 2, west is 3
	def move(self, movement):
		direction = movement[0]
		distance = int(movement[1:])
		if direction == 'R':
			self.d = (self.d + 1) % 4
		if direction == 'L':
			self.d = (self.d - 1) % 4
		if self.d == 0:
			self.y += distance
		elif self.d == 1:
			self.x += distance
		elif self.d == 2:
			self.y -= distance
		elif self.d == 3:
			self.x -= distance
	def compute_distance(self):
		return abs(self.x) + abs(self.y)

def main():
	content = open('input.txt').read().strip()
	moves = content.split(', ')
	santa = Santa()
	for move in moves:
		santa.move(move)
	print(santa.compute_distance())

main()		
