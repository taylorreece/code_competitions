infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')

num_problems = int(infile.readline())

def list_to_int(l):
	return int("".join(str(x) for x in l))

def find_low(num, first_itteration=False):
	if not num:
		return num
	if first_itteration:
		new_num = [x if x != 0 else 10 for x in num]
		m = min(new_num)
	else:
		m = min(num)
	if m == 10:
		m = 0
	imin = len(num) - num[::-1].index(m) - 1
	if num[0] == m:
		return [num[0]] + find_low(num[1:])
	else:
		temp = num[0]
		num[0] = num[imin]
		num[imin] = temp
	return num
	
def find_high(num):
	if not num:
		return num
	m = max(num)
	imax = len(num) - num[::-1].index(m) - 1
	if num[0] == m:
		return [num[0]] + find_high(num[1:])
	else:
		temp = num[0]
		num[0] = num[imax]
		num[imax] = temp
	return num
	
for i in range(0,num_problems):
	number = int(infile.readline())
	low = list_to_int(find_low([int(i) for i in str(number)], first_itteration=True))
	high = list_to_int(find_high([int(i) for i in str(number)]))
	print("Case #%s: %s %s" % (i+1,low,high))
	outfile.write("Case #%s: %s %s\n" % (i+1,low,high))

infile.close()
outfile.close()