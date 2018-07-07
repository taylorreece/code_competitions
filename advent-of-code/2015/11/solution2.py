#!/usr/bin/python
import re

mystring = 'hxbxxyzz'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def passes(s):
	if 'i' in s or 'o' in s or 'l' in s:
		return False
	if len([m.group(0) for m in re.finditer(r'([a-z])\1',s)]) < 2:
		return False
	for i in range(24):
		if alphabet[i:i+3] in s:
			return True
	return False

def increment(s):
	if s[-1] == 'z':
		return increment(s[:-1]) + 'a'
	return s[:-1] + chr(ord(s[-1]) + 1)

mystring = increment(mystring) # so we don't use the already working password

while not passes(mystring):
	mystring = increment(mystring)

print mystring
