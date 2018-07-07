#!/usr/bin/python

with open('input.txt', 'r') as f:
	total = 0
	for line in f:
		l,w,h = line.split('x')
		l,w,h = int(l),int(w),int(h)
		total = total + 2 * (l + w + h) - 2 * max(l,w,h) + l*w*h 
	print total

