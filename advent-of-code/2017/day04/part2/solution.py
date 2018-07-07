#!/usr/bin/env python3

import hashlib

count = 0

def hash(word):
    return hashlib.md5(''.join(sorted(word)).encode()).hexdigest()

with open("input.txt", 'r') as f:
    for line in f.readlines():
        line = line.strip()
        hashes = [hash(word) for word in line.split(' ')]
        if len(set(hashes)) == len(hashes):
            count += 1
print(count)
