#!/usr/bin/python3

steps = 100

def print_game(game):
	for row in game:
		print(row)
	print('='*len(game[0]))

def step(game):
	ret = list()
	ret.append('.'*len(game[0]))
	for i in range(1,len(game)-1):
		newline = list()
		newline.append('.')
		for j in range(1,len(game[0])-1):
			total = sum([a[j-1:j+2].count('#') for a in game[i-1:i+2]])
			if (game[i][j] == '#' and total in [3,4]) or (game[i][j] == '.' and total == 3):
				newline.append('#')
			else:
				newline.append('.')
		newline.append('.')
		ret.append(''.join(newline))
	ret.append('.'*len(game[0]))
	return ret


game = list()
with open('input.txt', 'r') as f:
	for line in f:
		game.append('.' + line.rstrip() + '.')

game.append(   '.'*len(game[0]))
game.insert(0, '.'*len(game[0]))

for i in range(steps):
	print('Running step %s' % i)
	game = step(game)

print(''.join(game).count('#'))

