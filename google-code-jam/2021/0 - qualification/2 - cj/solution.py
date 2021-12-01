#!/usr/bin/env python3

num_problems = int(input())

def solve(X, Y, mystring):
    cjs = 0
    jcs = 0
    for i in range(len(mystring)-1):
        if mystring[i:i+2] == 'CJ':
            cjs += 1
        if mystring[i:i+2] == 'JC':
            jcs += 1
    return X * cjs + Y * jcs

for i in range(num_problems):
    X, Y, mystring = input().split()
    X = int(X)
    Y = int(Y)
    mystring = mystring.replace('?','')
    print(f"Case #{i+1}: {solve(X, Y, mystring)}")