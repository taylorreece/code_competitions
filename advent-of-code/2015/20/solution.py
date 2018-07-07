#!/usr/bin/python

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Set score to an order of magnitude less than requested
target = 2900000

score = 0
house = 0

while score <= target:
	house = house + 1
	score = 1
	factors = prime_factors(house)
	for i in set(factors):
		score = score * sum([i**j for j in range(factors.count(i)+1)])
print(house)
