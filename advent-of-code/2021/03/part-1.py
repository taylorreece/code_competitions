#!/usr/bin/env python3

inputs = []

def mostCommon(column):
  if column.count('0') > column.count('1'):
    return '0'
  return '1'

with open('input.txt', 'r') as infile:
  for line in infile:
    inputs.append(list(line.strip()))

columns = list(zip(*inputs))

common = ''.join(map(mostCommon, columns))

print(int(common, 2) * (int('1'*len(common), 2) - int(common,2)))