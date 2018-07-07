#!/usr/bin/env python3

import os

# Deals with printing to stdout, and to a file
class P:
    def __init__(self):
        if os.path.exists('output.txt'):
            os.unlink('output.txt')
    def out(self, s):
        print(s)
        with open('output.txt', 'a') as f:
            f.write('{}\n'.format(s))
p = P()

# Define solve(a,b,c...) here
def solve(p, f):
    flips = 0
    for i in range(len(p)-f+1):
        if p[i] == 0:
            flips += 1
            for j in range(i, i+f):
                p[j] = 1 - p[j]
    if 0 in p:
        return 'IMPOSSIBLE'
    return flips

# File input stuff here
with open('input.txt') as f:
    num_problems = int(f.readline())
    # Process stuff here, and write out
    for i in range(num_problems):
        pancakes, flipper = f.readline().split(' ')
        flipper = int(flipper)
        p.out('Case #{}: {}'.format(
            i+1,
            solve(
                [0 if x=='-' else 1 for x in pancakes],
                int(flipper)
            )
        ))
