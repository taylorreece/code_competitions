#!/usr/bin/env python3

count = 0

with open("input.txt", 'r') as f:
    for line in f.readlines():
        line = line.strip()
        words = line.split(' ')
        if len(set(words)) == len(words):
            count += 1
print(count)
