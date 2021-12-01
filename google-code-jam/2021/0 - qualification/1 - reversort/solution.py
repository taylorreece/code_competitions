#!/usr/bin/env python3

num_problems = int(input())

def solve(myList):
    if len(myList) == 1:
        return 0
    if len(myList) == 2:
        if myList[0] < myList[1]:
            return 1
        return 2
    smallest_idx = myList.index(min(myList))
    return 1 + smallest_idx + solve(myList[:smallest_idx][::-1] + myList[smallest_idx+1:])


for i in range(num_problems):
    _, myList = input(), list(map(int, input().split()))
    print(f"Case #{i+1}: {solve(myList)}")