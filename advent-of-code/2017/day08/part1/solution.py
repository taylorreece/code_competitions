#!/usr/bin/env python3

vals = dict()

with open('input.txt','r') as f:
    for line in f.readlines():
        operand, operator, delta, _, operand2, operator2, val2 = line.split()
        if operand not in vals:
            vals[operand] = 0
        if operand2 not in vals:
            vals[operand2] = 0
        query = 'vals["{}"] {} {}'.format(operand2, operator2, val2)
        if eval(query):
            if operator == 'inc':
                vals[operand] += int(delta)
            else:
                vals[operand] -= int(delta)
print(max(vals.values()))
