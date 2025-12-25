class Node:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.next = None

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [None] * num_vertices  # initialize adjacency list

    def add_edge(self, src, dest, weight):
        # Add edge src -> dest
        new_node = Node(dest, weight)
        new_node.next = self.adj_list[src]
        self.adj_list[src] = new_node
    
    def print_graph(self):
        for i in range(self.num_vertices):
            print(f"{i}:", end=" ")
            temp = self.adj_list[i]
            while temp:
                print(f"({temp.value}, weight={temp.weight})", end=" -> ")
                temp = temp.next
            print("None")

    

# Example usage
g = Graph(4)   # 4 vertices: 0,1,2,3

g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 4)
g.print_graph()
print(g.max_vertex_sum())

