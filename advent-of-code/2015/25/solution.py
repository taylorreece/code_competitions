#!/usr/bin/python3

row = 2978
column = 3083
current = 20151125

def sum_one_to_n(n):
	return n * (n+1) / 2

def get_order_val(row,column):
	return int(sum_one_to_n(column+row-2) + column)

position = get_order_val(row, column)
for i in range(1,position):
	current = (current * 252533) % 33554393

print(current)
