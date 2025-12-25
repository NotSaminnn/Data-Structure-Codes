vertices = 5
edges = [(0, 1, 3), (0, 2, 5), (1, 2, 2), (1, 3, 4), (2, 4, 1), (3, 4, 6), (1, 4, 7)]

def adj_matrix(vertices, edges):
    matrix = [[0]*vertices for i in range(vertices)]
    for i in edges:
        u,v,w = i
        matrix[u][v] = w
    return matrix

matrix = adj_matrix(vertices, edges)
print(matrix)

def undirectional_matrix(matrix):
    matrix2 = [[0]*vertices for i in range(vertices)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                matrix2[j][i] = matrix[i][j]
                matrix2[i][j] = 0

    return matrix2

print(undirectional_matrix(matrix))