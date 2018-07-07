#!/usr/bin/python

with open('input.txt', 'r') as f:
	total = 0
	for line in f:
		l,w,h = line.split('x')
		l,w,h = int(l),int(w),int(h)
		total = total + 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,l*h)
	print total

