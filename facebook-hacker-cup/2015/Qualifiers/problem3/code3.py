import copy

graph = {1: [2, 3],
             2: [3, 4],
             3: [4],
             4: [3],
             5: [3],
             6: [3]}

def find_shortest_path(graph, start, end):
	steps = 1
	seen = []
	new = [start]
	found = False
	while not found:
		last = copy.copy(new)
		for l in last:
			seen.append(l)
		new = []
		for n in last:
			for g in graph[n]:
				if end == g:
					found = True
					break
				if g not in seen and g not in last:
					new.append(g)
			if found:
				break
		steps = steps + 1
		if not new:
			return False
	return steps
	
	
print(find_shortest_path(graph, 1, 3))