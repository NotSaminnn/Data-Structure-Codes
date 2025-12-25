
def adj_list(vertices, edges):
    adj_list=[[] for i in range(vertices)]

    for i in edges:
        u,v,w = i
        adj_list[u] +=[(v,w)]
    return adj_list

def max_weight_list(matrix):
    max_weight=-99999999
    max_edge = None
    for i in range(len(matrix)):
        total=0
        for j in range(len(matrix[i])):
            u,v= matrix[i][j]
            total += v
        if total > max_weight:
            max_weight = total
            max_edge = i
    return max_edge, max_weight


def max_degree_list(matrix):
    max_degree= -99999
    max_vertex = None

    for i in range(len(matrix)):
        deg = len(matrix[i])
        if deg > max_degree:
            max_degree = deg
            max_vertex = i

    return max_vertex, max_degree
vertices = 5
edges = [(0, 1, 3), (0, 2, 5), (1, 2, 2), (1, 3, 4), (2, 4, 1), (3, 4, 6), (1, 4, 7)]

print(adj_list(vertices, edges))

