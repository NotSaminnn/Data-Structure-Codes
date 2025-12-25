vertices = 5
edges = [(0, 1, 3), (0, 2, 5), (1, 2, 2), (1, 3, 4), (2, 4, 1), (3, 4, 6), (1, 4, 7)]


def adj_matrix(vertices, edges):
    matrix = [[0]*vertices for i in range(vertices)]
    for i in edges:
        u,v,w= i
        matrix[u][v] = w
        matrix[v][u] = w
    return matrix
matrix = adj_matrix(vertices, edges)

def max_weight_matrix(matrix):
    max_weight=-99999999
    max_edge = None
    for i in range(len(matrix)):
        total=0
        for j in range(len(matrix)):
            total += matrix[i][j]
        if total > max_weight:
            max_weight = total
            max_edge = i
    return max_edge, max_weight

print(max_weight_matrix(matrix))


