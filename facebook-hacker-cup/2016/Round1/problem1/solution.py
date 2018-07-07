#!/usr/bin/env python3

# 2017 Facebook Hacker Cup
# Round 1, Problem 1
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

def solve(days):
	total = 0
	options = []
	for i in range(len(days)):
		options += days[i]
		total += min(options)
		options.remove(min(options))
	return total

with open('input.txt','r') as f:
	num_cases = int(f.readline())
	for i in range(num_cases):
		num_days, _ = map(int,f.readline().split(' '))
		days = []
		for d in range(num_days):
			day_vals = sorted(map(int,f.readline().strip().split(' ')))
			day_vals = [day_vals[i]+1+i*2 for i in range(len(day_vals))]
			days.append(day_vals)
		write('Case #{}: {}'.format(i+1,solve(days)))
