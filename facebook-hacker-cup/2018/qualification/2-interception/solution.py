#!/usr/bin/env python3
out_file = open('output.txt', 'w')
DEBUG = True

def debug(line):
    if DEBUG:
        print(line)

def output(line):
    print(line)
    out_file.write(str(line) + '\n')

def solve(coefficients):
    debug("Coefficients: %s" % coefficients)
    l = len(coefficients)
    cf_added = [
        coefficients[index] + l - index
        for index in range(0,l)
    ]
    cf_added[-1] = 0
    cf_added[0] = coefficients[0]
    first_zero = cf_added.index(0)
    if first_zero % 2:
        return [0.0]
    else:
        return []


with open('input.txt', 'r') as in_file:
    T = int(in_file.readline())
    for _ in range(T):
        N = int(in_file.readline())
        coefficients = list()
        for __ in range(N+1):
            coefficients.append(int(in_file.readline()))
        solutions = solve(coefficients)
        output('Case #{}: {}'.format(_+1, len(solutions)))
        for solution in solutions:
            output(solution)

out_file.close()