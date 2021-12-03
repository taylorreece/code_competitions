#!/usr/bin/env python3

linecount = 0

inputs = []

def mostCommon(column):
  if column.count('0') > column.count('1'):
    return '0'
  return '1'

def find_oxygen(inputs, idx=0):
  if len(inputs) == 1:
    return inputs[0]
  common = mostCommon(list(zip(*inputs))[idx])
  return find_oxygen(list(filter(lambda input: input[idx] == common, inputs)), idx+1)

def find_co2(inputs, idx=0):
  if len(inputs) == 1:
    return inputs[0]
  common = '0' if mostCommon(list(zip(*inputs))[idx]) == '1' else '1'
  return find_co2(list(filter(lambda input: input[idx] == common, inputs)), idx+1)


with open('input.txt', 'r') as infile:
  for line in infile:
    inputs.append(list(line.strip()))

oxygen = int(''.join(find_oxygen(inputs)), 2)
co2 = int(''.join(find_co2(inputs)), 2)

print(oxygen)
print(co2)

print(oxygen * co2)