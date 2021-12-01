#!/usr/bin/env python3

count = 0

with open('input.txt', 'r') as infile:
  m = [infile.readline(), infile.readline(), infile.readline(), infile.readline()]
  while m[3]:
    if int(m[3]) > int(m[0]):
      count += 1
    m = m[1:]
    m.append(infile.readline())
print(count)