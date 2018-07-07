#!/usr/bin/env python3

# 2017 Facebook Hacker Cup
# Round 1, Problem 2
# https://www.facebook.com/hackercup/round/1825579961046099/

# Solution by Taylor Reece

import os, sys

if os.path.exists('output.txt'):
	os.remove('output.txt')

def write(stuff):
	original = sys.stdout
	print(stuff)
	sys.stdout = open('output.txt','a')
	print(stuff)
	sys.stdout = original

def solve(A):
	return A

with open('input.txt','r') as f:
	num_cases = int(f.readline())
	for i in range(num_cases):
		a = f.readline().strip()
		write('Case #{}: {}'.format(i+1,solve(a)))
