#!/usr/bin/env python3

def solve(mySize, myCost):
    left = False
    myMin = mySize - 1
    myMax = (mySize ** 2 + mySize) / 2 - 1
    if (myCost < myMin or myCost > myMax):
        return "IMPOSSIBLE"
    left = True
    leftList = []
    rightList = []
    for i in range(1,mySize+1):
        placementCost = mySize - i + 1
        if placementCost + mySize - i - 1 <= myCost:
            left = not left
            myCost -= placementCost - 1
        if left:
            leftList += [i]
        else:
            rightList = [i] + rightList
        myCost -= 1
    return ' '.join(map(str, leftList + rightList))

num_problems = int(input())

for i in range(num_problems):
    mySize, myCost = map(int, input().split())
    print(f"Case #{i+1}: {solve(mySize, myCost)}")