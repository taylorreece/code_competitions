#!/usr/bin/python

target = 29000000

houses = [0] * (target/10)

for i in range(1,target/10):
	for j in range(i,target/10,i):
		if j/i <= 50:
			houses[j] = houses[j] + i*11

for i in range(1,target/10):
	if houses[i] > target:
		print(i)
		break
