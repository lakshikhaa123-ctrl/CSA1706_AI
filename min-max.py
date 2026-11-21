
def minimax(tree, node, maximizing):
    if node not in tree:
        return node

    values = [minimax(tree, child, not maximizing)
              for child in tree[node]]

    if maximizing:
        return max(values)
    else:
        return min(values)

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [2, 3],
    'E': [5, 9],
    'F': [0, 1],
    'G': [5, 1]
}

print("Minimax Value:", minimax(tree, 'A', True))

