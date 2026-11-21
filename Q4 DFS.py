graph = {
    1: [2, 3],
    2: [1, 5, 6],
    3: [1, 7, 4],
    4: [3, 8],
    5: [2],
    6: [2],
    7: [3, 8],
    8: [7, 4]
}

def DFS(node, visited):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            DFS(neighbour, visited)

visited = []
DFS(1, visited)
print("DFS:", visited)
