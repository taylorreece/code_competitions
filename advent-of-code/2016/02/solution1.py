#!/usr/bin/python

class Board:
	def __init__(self):
		self.board = [[1,2,3],[4,5,6],[7,8,9]]
		self.x = 1
		self.y = 1
		self.val = 5
	def move(self,move):
		if move == 'U': self.y = max(0,self.y-1)
		if move == 'D': self.y = min(2,self.y+1)
		if move == 'L': self.x = max(0,self.x-1)
		if move == 'R': self.x = min(2,self.x+1)
		self.val = self.board[self.y][self.x]

def main():
	b = Board()
	code = []
	with open('input.txt', 'r') as f:
		for line in f:
			line = line.strip()
			for c in line:
				b.move(c)
			code.append(b.val)
	print(''.join([str(x) for x in code]))

main()
