#!/usr/bin/python

import math

def solve(items):
    items.sort()
    trips = 0
    while items:
        if items[-1]*len(items)<50:
            return trips
        trips += 1
        heaviest = items[-1]
        if heaviest < 50:
            num_in_sack = math.ceil(50.0/heaviest)
            for i in range(int(num_in_sack)-1):
                items.remove(items[0])
        items.remove(heaviest)
    return trips


with open('input.txt') as f:
    numproblems = int(f.readline())
    for i in range(numproblems):
        numitems = int(f.readline())
        items = []
        for j in range(numitems):
            items.append(int(f.readline()))
        print('Case #{}: {}'.format(i+1,solve(items)))
