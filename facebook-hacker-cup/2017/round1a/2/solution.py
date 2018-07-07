#!/usr/bin/env python3

import os
import math
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
def solve(targets, ingredients):
    #print("========================================")
    sets = 0
    for i in ingredients[0]:
        estimate = math.floor(i / targets[0])
        possibilities = []
        for e in range(estimate-20, estimate+20):
            if e>0 and targets[0]*e*.9 <= i and i <= targets[0]*e*1.1:
                possibilities.append(e)
        possibilities = set(possibilities)
        to_remove = [0]
        solved = False
        #print("possibilities: %s" % possibilities)
        for p in possibilities:
            to_remove = [0]
            if not solved:
                #print("Testing possibility %s" % p)
                for j in range(1,len(targets)):
                    removed = False
                    for k in ingredients[j]:
                        #print("%s <= %s <= %s" % (targets[j]*p*.9, k, targets[j]*p*1.1))
                        if targets[j]*p*.9 <= k and k <= targets[j]*p*1.1 and not removed:
                            #print("found %s in %s, %s, %s, %s" % (k, ingredients[j], j, to_remove, removed))
                            to_remove.append(k)
                            removed = True
                            #print("found %s in %s, %s, %s, %s" % (k, ingredients[j], j, to_remove, removed))
                #print("==> %s - %s" % (to_remove, targets))
                if len(to_remove) == len(targets):
                    #print(to_remove)
                    sets += 1
                    solved = True
                    for k in range(1,len(targets)):
                        #print(ingredients[k])
                        ingredients[k].remove(to_remove[k])
                    #print("After remove, ingredients are %s" % ingredients)
    return sets

# File input stuff here
with open('input.txt') as f:
    num_problems = int(f.readline())
    # Process stuff here, and write out
    for i in range(num_problems):
        N, P = list(map(int, f.readline().split(' ')))
        targets = list(map(int, f.readline().split(' ')))
        ingredients = []
        for j in range(N):
            ingredients.append(sorted(list(map(int, f.readline().split(' ')))))
        p.out('Case #{}: {}'.format(
            i+1,
            solve(
                targets, ingredients
            )
        ))
