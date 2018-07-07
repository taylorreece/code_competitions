#!/usr/bin/python

class Board:
	def __init__(self):
		self.board = [[None,None,1,None,None],[None,2,3,4,None],[5,6,7,8,9],[None,'A','B','C',None],[None,None,'D',None,None]]
		self.x = 0
		self.y = 2
		self.val = 5
	def move(self,move):
		if move == 'U' and self.board[max(0,self.y-1)][self.x]: self.y = max(0,self.y-1)
		if move == 'D' and self.board[min(4,self.y+1)][self.x]: self.y = min(4,self.y+1)
		if move == 'L' and self.board[self.y][max(0,self.x-1)]: self.x = max(0,self.x-1)
		if move == 'R' and self.board[self.y][min(4,self.x+1)]: self.x = min(4,self.x+1)
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
