#!/usr/bin/python

import math

def distance(P1, P2):
    return math.sqrt((P1[0]-P2[0])**2 + (P1[1]-P2[1])**2)

def angle(x,y):
    if x == 50:
        if y > 50:
            return 0
        return 180
    if y == 50:
        if x > 50:
            return 90
        return 270
    extra = 0
    if x < 50 and y < 50:
        extra = 180
    if x < 50 and y > 50:
        extra = 270
    if x > 50 and y < 50:
        extra = 90
    return extra + math.atan(abs(x-50)/abs(y-50))/(math.pi)*180

def solve(P, X, Y):
    if X==50 and Y==50 and P>0:
        return 'black'
    if distance((50,50),(X,Y)) <= 50 and angle(X,Y) <= P*3.6:
        return 'black'
    return 'white'

with open('input.txt') as f:
    numproblems = int(f.readline())
    for i in range(numproblems):
        P,X,Y = f.readline().strip().split(' ')
        print('Case #%s: %s' % (i+1,solve(int(P),int(X),int(Y))))
