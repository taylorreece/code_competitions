#!/usr/bin/python

def has_three_vowels(word):
	count = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')
	return count >= 3

def has_double_letter(word):
	for i in range(len(word)-1):
		if word[i] == word[i+1]:
			return True
	return False

def contains_bad_combo(word):
	bad_combos = ['ab', 'cd', 'pq', 'xy']
	for bc in bad_combos:
		if bc in word:
			return True
	return False

def valid(word):
	return has_three_vowels(word) and has_double_letter(word) and not contains_bad_combo(word)

with open('input.txt', 'r') as f:
	count = 0
	for line in f:
		if valid(line):
			count = count + 1
	print count
