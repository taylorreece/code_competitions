#!/usr/bin/env python3

import re
DICE_REGEX = r'(\d*)d(\d*)([+-]\d*)?'

def getProb(S,N,threshold):
    x = [1]*S
    for i in range(1,N):
        tmp = []
        for j in range((i+1)*S):
            tmp.append(sum(x[max(0,j-S):j]))
        x = tmp
    return sum([x[i] for i in range(len(x)) if i+1 >= threshold])/sum(x)

def solve(min_damage, spells):
    max_probability = 0.0
    for spell in spells:
        dice_vals = re.findall(DICE_REGEX, spell)[0]
        N,S = map(int,dice_vals[:2])
        modifier = '+0'
        if dice_vals[2] != '':
            modifier = int(dice_vals[2])
        prob = getProb(S, N, eval('%s-%s' % (min_damage, modifier)))
        if prob > max_probability:
            max_probability = prob
    return format(max_probability, '.6f')

with open('input.txt') as f:
    num_problems = int(f.readline())
    for i in range(num_problems):
        min_damage, _ = map(int,f.readline().split(' '))
        spells = f.readline().strip().split(' ')
        print('Case #%s: %s' % (i+1, solve(min_damage, spells)))
