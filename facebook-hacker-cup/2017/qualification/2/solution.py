#!/usr/bin/env python3

import os

def Alphabetical(word):
    return word==''.join(sorted(word))

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


# Define solve() here
def solve(a):
    for i in range(len(a)-1,0,-1):
        if a[i] < a[i-1]:
            a = a[0:i] + [9]*(len(a)-i)
            a[i-1] -= 1
    return int(''.join(map(str,a)))

# File input stuff here
with open('input.txt') as f:
    num_problems = int(f.readline())
    # Process stuff here, and write out
    for i in range(num_problems):
        num = f.readline().strip()
        p.out('Case #{}: {}'.format(
            i+1,
            solve(
                #int(f.readline())
                list(map(int,list(num)))
            )
        ))
