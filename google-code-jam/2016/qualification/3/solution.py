#!/usr/bin/python3

import itertools, re

def prime_factor(number):
	for i in range(2,100):
		if number % i == 0:
			return i
	return False

def nonprime_factor(num, base):
	number = sum([int(num[len(num)-i-1]) * (base ** i) for i in range(len(num))])
	factor = prime_factor(number)
	if factor:
		return str(factor)
	return None

def solve(N,J):
	solved = 0
	for i in range((N-2)**2):
		num = '1' + bin(i)[2:].rjust(N-2,'0') + '1'
		npfs = [None] * 9
		works = True
		for i in range(2,11):
			npf = nonprime_factor(num, i)
			if not npf:
				works = False
			npfs[i-2] = npf
		if works:
			solved = solved + 1
			print(num, ' '.join(npfs))	
		if solved == J: # We got to the end!
			return

with open('input.txt', 'r') as f:
	num_problems = int(f.readline())
	for i in range(num_problems):
		N,J = [int(i) for i in f.readline().rstrip().split(' ')]
		print('Case #%s:' % (i+1))
		solve(N,J)
