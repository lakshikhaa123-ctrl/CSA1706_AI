
import heapq

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'E', 'H'],
    'D': ['A', 'H'],
    'H': ['C', 'D', 'G'],
    'E': ['B', 'C', 'F'],
    'F': ['E', 'G'],
    'G': ['H', 'F']
}

h = {
    'A': 40, 'B': 32, 'C': 25,
    'D': 35, 'H': 17, 'E': 19,
    'F': 10, 'G': 0
}

def gbfs(start, goal):
    pq = [(h[start], start, [start])]
    visited = set()

    while pq:
        _, node, path = heapq.heappop(pq)

        if node == goal:
            print("Path:", path)
            return

        if node not in visited:
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(
                        pq, (h[neighbour], neighbour,
                             path + [neighbour])
                    )

    print("Goal not found")

gbfs('A', 'G')

