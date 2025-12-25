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
                matrix2[i][j] = matrix[i][j]
                matrix2[j][i] = matrix[i][j]  # Make it symmetric
    return matrix2

print(undirectional_matrix(matrix))



ADJ_list


vertices = 5
edges = [(0, 1, 3), (0, 2, 5), (1, 2, 2), (1, 3, 4), (2, 4, 1), (3, 4, 6), (1, 4, 7)]

def adj_list(vertices, edges):
    adj_list=[[] for i in range(vertices)]
    for i in edges:
        u,v,w = i
        adj_list[u] +=[(v,w)]
    return adj_list

print("Directed adjacency list:")
directed_adj = adj_list(vertices, edges)
print(directed_adj)

def undirectional_list(adj_list_directed):
    adj_list2 = [[] for i in range(len(adj_list_directed))]
    
    for i in range(len(adj_list_directed)):
        for j in adj_list_directed[i]:
            u, w = j
            adj_list2[i].append((u, w))
            adj_list2[u].append((i, w))
    
    return adj_list2

print("\nUndirected adjacency list:")
print(undirectional_list(directed_adj))
            

    


