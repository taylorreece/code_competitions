#!/usr/bin/env python3
out_file = open('output.txt', 'w')

def output(line):
    out_file.write(line + '\n')
    print(line)

def ethans_algorithm(word1, word2):
    i = j = 0
    while True:
        if i >= len(word1):
            return True
        if j >= len(word2):
            return False
        if word1[i] == word2[j]:
            i += 1
            j += 1
        elif i == 0:
            j += 1
        else:
            i = 0

def solve(word):
    for i in range(len(word)):
        if not ethans_algorithm(word, word[:i]+word):
            return word[:i]+word
    return 'Impossible'

with open('input.txt', 'r') as in_file:
    T = int(in_file.readline())
    for t in range(T):
        output('Case #{}: {}'.format(t+1, solve(in_file.readline().strip())))

out_file.close()