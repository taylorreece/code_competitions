#!/usr/bin/python

import md5

with open('input.txt', 'r') as f:
	for line in f:
		num = 1
		while True:
			if md5.new(line.strip() + str(num)).hexdigest().startswith('000000'):
				print num
				break;
			num = num + 1
