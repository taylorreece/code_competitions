import hashlib

infile = open('input.txt','r')
outfile = open('output.txt','w')
G = []

def subset_sum(numbers, target, index, partial=[]):
	global G
	s = sum([x[index] for x in partial])
	if s == target: 
		G.append(partial)
	if s >= target:
		return
	for i in range(len(numbers)):
		n = numbers[i]
		remaining = numbers[i+1:]
		subset_sum(remaining, target, index, partial + [n])
		
		
def solve(goals,foods):
	global G
	G = []
	subset_sum(foods,goals[0],0)
	G_protein = [hashlib.sha224(str(x).encode('utf-8')).hexdigest() for x in G]
	G = []
	subset_sum(foods,goals[1],1)
	G_carbohydrates = [hashlib.sha224(str(x).encode('utf-8')).hexdigest() for x in G]
	G = []
	subset_sum(foods,goals[1],1)
	G_fat = [hashlib.sha224(str(x).encode('utf-8')).hexdigest() for x in G]
	intersection = set.intersection(set(G_protein),set(G_carbohydrates),set(G_fat))
	if list(intersection):
		return True
	return False

	
num_problems = int(infile.readline())
for i in range(0, num_problems):
	goals = list(map(int, infile.readline().split(' ')))
	num_foods = int(infile.readline())
	foods = []
	for j in range(0, num_foods):
		foods.append(list(map(int, infile.readline().split(' '))) + [j])
	if solve(goals, foods):
		print("Case #%s: yes" % (i+1))
		outfile.write("Case #%s: yes\n" % (i+1))
	else:
		print("Case #%s: no" % (i+1))
		outfile.write("Case #%s: no\n" % (i+1))