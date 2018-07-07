#!/usr/bin/python

def has_double_instance(word):
	for i in range(len(word)-2):
		if word.count(word[i] + word[i+1]) > 1:
			return True
	return False

def repeat_with_spacer(word):
	for i in range(len(word)-2):
		if word[i] == word[i+2]:
			return True
	return False

def valid(word):
	return has_double_instance(word) and repeat_with_spacer(word)

with open('input.txt', 'r') as f:
	count = 0
	for line in f:
		if valid(line):
			count = count + 1
	print count
