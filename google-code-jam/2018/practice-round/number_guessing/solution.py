#!/usr/bin/env python3
num_cases = int(input())

for n in range(num_cases):
    a,b = [int(x) for x in input().split()]
    n = int(input())
    result = ''
    while result != 'CORRECT':
        guess = int((a+b)/2)
        print(guess)
        result = input()
        if result == 'TOO_SMALL':
            a = guess+1
        elif result == 'TOO_BIG':
            b = guess-1
    