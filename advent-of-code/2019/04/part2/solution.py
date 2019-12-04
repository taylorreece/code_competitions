#!/usr/bin/env python3

with open('input.txt', 'r') as infile:
    my_min, my_max = [int(x) for x in infile.read().strip().split('-')]

count = 0
for i in range(10):
    for j in range(i, 10):
        for k in range(j, 10):
            for l in range(k, 10):
                for m in range(l, 10):
                    for n in range(m, 10):
                        if ((i == j and j != k) or
                            (i != j and j == k and k != l) or 
                            (j != k and k == l and l != m) or
                            (k != l and l == m and m != n) or
                            (l != m and m == n)):
                            my_num = i*100000 + j * 10000 + k * 1000 + l * 100 + m * 10 + n
                            if my_min <= my_num and my_num <= my_max:
                                count += 1
print(f'Count: {count}')