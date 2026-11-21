
import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 3},
    'C': {'E': 5},
    'D': {'F': 2, 'G': 1},
    'E': {'G': 3},
    'F': {'G': 1},
    'G': {}
}

h = {
    'A': 5, 'B': 6, 'C': 4,
    'D': 3, 'E': 3, 'F': 1, 'G': 0
}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node == goal:
            print("Path:", path)
            print("Cost:", cost)
            return

        for next_node, weight in graph[node].items():
            new_cost = cost + weight
            new_f = new_cost + h[next_node]

            heapq.heappush(
                pq, (new_f, new_cost, next_node,
                     path + [next_node])
            )

astar('A', 'G')
