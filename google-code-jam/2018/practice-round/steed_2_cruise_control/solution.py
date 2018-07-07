#!/usr/bin/env python3

def solve():
    d, n = map(int, input().split())
    longest_horse_time = 0
    for _ in range(n):
        k, s = map(int, input().split())
        horse_time = (d - k) / s
        longest_horse_time = max(horse_time, longest_horse_time)
    return d / longest_horse_time

num_problems = int(input())
for n in range(num_problems):
    print("Case #{}: {}".format(n+1, solve()))