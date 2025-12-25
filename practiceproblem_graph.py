#ques-7

vertices = 5
edges = [(0, 1, 3), (0, 2, 5), (1, 2, 2), (1, 3, 4), (2, 4, 1), (3, 4, 6), (1, 4, 7)]

def adj_list(vertices, edges):
    adj_list=[[] for i in range(vertices)]

    for i in edges:
        u,v,w = i
        adj_list[u] +=[(v,w)]
        adj_list[v] +=[(u,w)]
    return adj_list

def max_weight_list(matrix):
    max_weight=-99999999
    max_edge = None
    for i in range(len(matrix)):
        total=0
        for j in range(len(matrix[i])):
            v,w = matrix[i][j]  
            total += 1
        if total > max_weight:
            max_weight = total
            max_edge = i
    x=list_maker(matrix,max_edge)

    return max_edge, x

def list_maker(matrix, max_edge):
    count=0
    for i in range(len(matrix[max_edge])):
        v,w = matrix[max_edge][i]
        if w > 5:
            count += 1
    
    result = [0] * count
    index = 0
    
    for i in range(len(matrix[max_edge])):
        v,w = matrix[max_edge][i]
        if w > 5:
            result[index] = (v, w)
            index += 1
    
    return result

print(max_weight_list(adj_list(vertices, edges)))




#ques-9

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