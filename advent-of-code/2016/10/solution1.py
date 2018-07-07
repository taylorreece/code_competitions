#!/usr/bin/python

import re

target = [17,61]

numbots = 300

bots = [[] for i in range(numbots)]
botinstructions = [[] for i in range(numbots)]

instructions = []

with open('input.txt') as f:
	for line in f:
		instructions.append(line.strip())

for i in instructions:
	match = re.match(r'^value ([0-9]*) goes to bot ([0-9]*)', i)
	if match:
		value, botid = int(match.group(1)), int(match.group(2))	
		bots[botid] = sorted(bots[botid] + [value])
	else:
		match = re.match(r'bot ([0-9]*) gives low to ([a-z]*) ([0-9]*) and high to ([a-z]*) ([0-9]*)', i)
		botinstructions[int(match.group(1))] = match.groups()[1:]

while target not in bots:
	for x in [x for x in range(numbots) if len(bots[x]) == 2]:
		i = botinstructions[x]
		if i[0] == 'bot':
			bots[int(i[1])] = sorted(bots[int(i[1])] + [min(bots[x])])
		if i[2] == 'bot':
			bots[int(i[3])] = sorted(bots[int(i[3])] + [max(bots[x])])
		bots[x] = []

print(bots.index(target))	
