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
def solve(m):
    go = True
    while go:
        for i in range(len(m)):
            if len(m[i])>1 and m[i][0] == '?' and m[i][1] != '?':
                m[i][0] = m[i][1]
            for j in range(1,len(m[i])):
                if m[i][j] == '?':
                    if m[i][j-1] != '?':
                        m[i][j] = m[i][j-1]
                    elif j < len(m[i])-1:
                        m[i][j] = m[i][j+1]

        go = False
        if '?' in m[0]:
            go = True
            if len(set(m[0])) == 1:
                m[0] = m[1]
        for i in range(1,len(m)):
            if '?' in m[i]:
                if len(set(m[i])) == 1:
                    if len(set(m[i-1])) != 1 or m[i-1][0]!='?':
                        m[i] = m[i-1]
                    elif i < len(m)-1:
                        m[i] = m[i+1]
                go = True
    return '\n'.join([''.join(x) for x in m])


# File input stuff here
with open('input.txt') as f:
    num_problems = int(f.readline())
    # Process stuff here, and write out
    for i in range(num_problems):
        R,C = map(int,f.readline().split(' '))
        m = []
        for j in range(R):
            m.append(list(f.readline().strip()))
        p.out('Case #{}:\n{}'.format(
            i+1,
            solve(m)
        ))
