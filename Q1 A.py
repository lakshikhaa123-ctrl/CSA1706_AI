
import heapq

graph = {
    'S': {'A': 3, 'D': 1},
    'A': {'S': 3, 'B': 4, 'D': 5},
    'B': {'A': 4, 'C': 4, 'E': 5},
    'C': {'B': 4},
    'D': {'S': 1, 'A': 5, 'E': 2},
    'E': {'D': 2, 'B': 5, 'F': 4},
    'F': {'E': 4, 'G': 3},
    'G': {'F': 3}
}

h = {
    'S': 15.3, 'A': 10.1, 'B': 5.8,
    'C': 3.4, 'D': 9.2, 'E': 7.1,
    'F': 3.5, 'G': 0
}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node == goal:
            print("Path:", path)
            print("Cost:", cost)
            return

        for neighbour, weight in graph[node].items():
            new_cost = cost + weight
            new_f = new_cost + h[neighbour]

            heapq.heappush(
                pq, (new_f, new_cost, neighbour,
                     path + [neighbour])
            )

astar('S', 'G')
