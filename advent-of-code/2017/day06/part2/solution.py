#!/usr/bin/env python3
import hashlib
with open('input.txt', 'r') as f:
    banks = [int(x) for x in f.readline().split()]

seen = dict()
count = 0
while hashlib.md5(','.join(map(str,banks)).encode()).hexdigest() not in seen:
    seen[hashlib.md5(','.join(map(str,banks)).encode()).hexdigest()] = count
    to_distribute = max(banks)
    index = banks.index(to_distribute)
    banks[index] = 0
    while to_distribute:
        index += 1
        if index >= len(banks):
            index = 0
        banks[index] += 1
        to_distribute -= 1
    count += 1

print(count - seen[hashlib.md5(','.join(map(str,banks)).encode()).hexdigest()])
