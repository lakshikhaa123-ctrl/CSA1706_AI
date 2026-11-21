def minimax(depth, node, maximizing, values, alpha, beta):

    if depth == 3:
        return values[node]

    if maximizing:
        best = float('-inf')

        for i in range(2):
            val = minimax(depth+1, node*2+i,
                          False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = minimax(depth+1, node*2+i,
                          True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [2, 3, 5, 9, 0, 1, 7, 5]

result = minimax(0, 0, True, values,
                 float('-inf'), float('inf'))

print("Optimal value:", result)
