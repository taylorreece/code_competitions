#!/usr/bin/env python3
out_file = open('output.txt', 'w')
DEBUG = True

def debug(line):
    if DEBUG:
        print(line)

def output(line):
    print(line)
    out_file.write(str(line) + '\n')

def solve(locations, K, V):
    debug("locations: %s\nK: %s\nV: %s" % (locations, K, V))
    start = K*(V-1) % len(locations)
    debug("start: %s" % start)
    ret = []
    if start + K > len(locations):
        ret += locations[:K-(len(locations)-start)]
    ret += locations[start:start+K]
    return ' '.join(ret)

with open('input.txt', 'r') as in_file:
    T = int(in_file.readline())
    for _ in range(T):
        N, K, V = map(int, in_file.readline().split())
        locations = list()
        for __ in range(N):
            locations.append(in_file.readline().strip())
        output('Case #{}: {}'.format(_+1, solve(locations, K, V)))

out_file.close()