graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2, 5],
    5: [2, 4]
}

def DFS(node, visited):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            DFS(neighbour, visited)

visited = []
DFS(1, visited)
print("DFS:", visited)
