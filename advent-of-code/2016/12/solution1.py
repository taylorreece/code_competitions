#!/usr/bin/python

a=0
b=0
c=0
d=0
instructions = []
with open('input.txt') as f:
	for line in f:
		instruction = line[:3]
		if instruction == 'cpy':
			_,x,y = line.strip().split(' ')
			instructions.append('%s=%s' % (y,x))
		if instruction == 'inc':
			instructions.append('%s+=1' % line[4])
		if instruction == 'dec':
			instructions.append('%s=%s-1' % (line[4],line[4]))
		if instruction == 'jnz':
			_,x,y = line.strip().split(' ')
			instructions.append('if %s!=0: loc+=%s-1' % (x,y))
loc = 0
while loc < len(instructions):
	exec(instructions[loc])
	loc+=1
print(a)
