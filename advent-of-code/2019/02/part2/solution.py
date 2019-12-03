#!/usr/bin/env python3



for i in range(0,100):
    for j in range(0,100):
        with open('input.txt', 'r') as infile:
            ints = [int(x) for x in infile.read().strip().split(',')]
        ints[1] = i
        ints[2] = j
        idx = 0
        while ints[idx] != 99:
            if ints[idx] == 1:
                ints[ints[idx+3]] = ints[ints[idx+1]] + ints[ints[idx+2]]
            elif ints[idx] == 2:
                ints[ints[idx+3]] = ints[ints[idx+1]] * ints[ints[idx+2]]
            idx += 4
        if ints[0] == 19690720:
            print(f'{i}, {j}: {i*100+j}')