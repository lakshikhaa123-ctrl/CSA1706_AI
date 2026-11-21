graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def DFS(node, visited):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            DFS(neighbour, visited)

visited = []
DFS('A', visited)
print("DFS:", visited)
