#!/usr/bin/python
import re
import json

total = 0

def get_total(a):
	'''Accepts a JSON object; recursively finds the total of the object'''
	t = 0
	if isinstance(a,int):
		return a
	if isinstance(a,list):
		for i in a:
			if isinstance(i,int):
				t = t + i
			else:
				t = t + get_total(i)
	if isinstance(a,dict):
		if 'red' in a.values():
			return 0
		for i in a.values():
			if isinstance(i,int):
				t = t + i
			else:
				t = t + get_total(i)
	return t
		

with open('input.txt') as f:
	for line in f:
		total = total + get_total(json.loads(line))

print total	
