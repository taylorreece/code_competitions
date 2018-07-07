#!/usr/bin/python

class Santa:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.d = 0 # North... East is 1, south is 2, west is 3
		self.history = [(0,0)]
	def move(self, movement):
		direction = movement[0]
		distance = int(movement[1:])
		if direction == 'R':
			self.d = (self.d + 1) % 4
		if direction == 'L':
			self.d = (self.d - 1) % 4
		if self.d == 0:
			for i in range(distance):
				self.y += 1
				if (self.x,self.y) in self.history:
					return (self.x,self.y)
				self.history.append((self.x,self.y))
		elif self.d == 1:
			for i in range(distance):
				self.x += 1
				if (self.x,self.y) in self.history:
					return (self.x,self.y)
				self.history.append((self.x,self.y))
		elif self.d == 2:
			for i in range(distance):
				self.y -= 1
				if (self.x,self.y) in self.history:
					return (self.x,self.y)
				self.history.append((self.x,self.y))
		elif self.d == 3:
			for i in range(distance):
				self.x -= 1
				if (self.x,self.y) in self.history:
					return (self.x,self.y)
				self.history.append((self.x,self.y))
	def compute_distance(self):
		return abs(self.x) + abs(self.y)

def main():
	content = open('input.txt').read().strip()
	moves = content.split(', ')
	santa = Santa()
	for move in moves:
		if santa.move(move) is not None:
			print(santa.compute_distance())
			break

main()		
