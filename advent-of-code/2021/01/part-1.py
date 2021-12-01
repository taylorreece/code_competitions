#!/usr/bin/env python3

count = 0

with open('input.txt', 'r') as infile:
  prev = infile.readline()
  next = infile.readline()
  while next:
    if int(next) > int(prev):
      count += 1
    prev = next
    next = infile.readline()
print(count)