

def max_degree_matrix(matrix):
    max_degree= -99999999
    max_vertex = None

    for i in range(len(matrix)):
        deg = 0
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                deg += 1
        if deg > max_degree:
            max_degree = deg
            max_vertex = i
    return max_vertex, max_degree

        
        

#example
vertices=5

edges = [(0,1),(0,2),(1,2),(1,3),(2,4),(3,4),(1,4)]
def adj_matrix(vertices, edges):
    matrix = [[0]*vertices for i in range(vertices)]
    for i in edges:
        u,v = i
        matrix[u][v] = 1
        matrix[v][u] = 1
    return matrix

matrix = adj_matrix(vertices, edges)
print(matrix)



# Adjacency List Representation

def adj_list(vertices, edges):
    adj_list=[[] for i in range(vertices)]

    for i in edges:
        u,v = i
        adj_list[u] +=[v]
        adj_list[v] +=[u]
    return adj_list

print(adj_list(vertices, edges))   


def max_degree_list(matrix):
    max_degree= -99999
    max_vertex = None

    for i in range(len(matrix)):
        deg = len(matrix[i])
        if deg > max_degree:
            max_degree = deg
            max_vertex = i

    return max_vertex, max_degree

print(max_degree_matrix(matrix))









