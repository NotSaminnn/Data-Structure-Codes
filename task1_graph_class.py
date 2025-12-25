class GraphMatrix:
    def __init__(self,vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.matrix = self.adj_matrix()

    def adj_matrix(self):
        matrix = [[0]*self.vertices for i in range(self.vertices)]
        for i in self.edges:
            u,v = i
            matrix[u][v] = 1
            matrix[v][u] = 1
        return matrix
    def max_degree_matrix(self):
        max_degree= -99999999
        max_vertex = None
        for i in range(len(self.matrix)):
            deg = 0
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1:
                    deg += 1
            if deg > max_degree:
                max_degree = deg
                max_vertex = i
        return max_vertex, max_degree
    def print_matrix(self):
        return self.matrix
    


vertices=5
edges = [(0,1),(0,2),(1,2),(1,3),(2,4),(3,4),(1,4)]

matrix = GraphMatrix(vertices, edges)

x=matrix.print_matrix()
y,z = matrix.max_degree_matrix()
print(y,z)




class GraphList:
    def __init__(self,vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adj_list = self.adj_list()
    def adj_list(self):
        adj_list=[[] for i in range(self.vertices)]
        for i in self.edges:
            u,v = i
            adj_list[u] +=[v]
            adj_list[v] +=[u]
        return adj_list
    def max_degree_list(self):
        max_degree= -99999
        max_vertex = None
        for i in range(len(self.adj_list)):
            deg = len(self.adj_list[i])
            if deg > max_degree:
                max_degree = deg
                max_vertex = i
        return max_vertex, max_degree
    def print_list(self):
        return self.adj_list
    
vertices=5
edges = [(0,1),(0,2),(1,2),(1,3),(2,4),(3,4),(1,4)]

adj_list = GraphList(vertices, edges)
x=adj_list.print_list()
y,z = adj_list.max_degree_list()
print(x)
print(y,z)