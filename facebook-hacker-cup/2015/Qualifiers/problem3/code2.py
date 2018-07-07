graph = {1: [2, 3],
             2: [3, 4],
             3: [4],
             4: [3],
             5: [3],
             6: [3]}

def find_shortest_path(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return path
	if not start in graph:
		return []
	shortest = []
	for node in graph[start]:
		if node not in path:
			newpath = find_shortest_path(graph, node, end, path)
			if newpath:
				if not shortest or len(newpath) < len(shortest):
					shortest = newpath
	return shortest
	
	
print(find_shortest_path(graph, 1, 3))