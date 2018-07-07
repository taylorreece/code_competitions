#!/usr/bin/env python3

import os
import time

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

def even(x):
    return x % 2 == 0

def odd(x):
    return not even(x)

# Define solve(a,b,c...) here
def solve(N, K):
    if K == 1:
        if N % 2:
            return (N//2, N//2)
        else:
            return (N//2, N//2-1)
    if even(N) and odd(K):
        new_N = N // 2 - 1
        new_K = K // 2
    if odd(N) and odd(K):
        new_N = N // 2
        new_K = K // 2
    if even(N) and even(K):
        new_N = N // 2
        new_K = K // 2
    if odd(N) and even(K):
        new_N = N // 2
        new_K = K // 2
    return solve(new_N, new_K)


# File input stuff here
with open('input.txt') as f:
    num_problems = int(f.readline())
    # Process stuff here, and write out
    for i in range(num_problems):
        N, K = map(int,f.readline().strip().split(' '))
        N, K = solve(N,K)
        p.out('Case #{}: {} {}'.format(
            i+1,
            N,
            K
        ))
