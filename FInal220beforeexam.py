
#Fall2024 labquiz-7
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
    def most_outgoing_edge(self):
        max_edge=-9999999
        max_vertex = None

        for i in range(len(self.adj_list)):
            count=0
            temp = self.adj_list[i]
            while temp != None:
                count += 1
                temp = temp.next

            if count > max_edge:
                max_edge = count
                max_vertex = i
        array=self.find_greater_weight(max_edge,max_vertex)

        return max_vertex,array
    def find_greater_weight(self,max_edge,max_vertex):
        array=[0]*max_edge
        temp=self.adj_list[max_vertex]
        count=0
        while temp!= None:
            if temp.weight >5:
                array[count]=temp.value
                count += 1
            temp = temp.next
        return array



# Example usage
g = Graph(5)   # 4 vertices: 0,1,2,3

g.add_edge(0, 1, 1)
g.add_edge(0, 2, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 3, 4)
g.add_edge(2, 4, 3)
g.add_edge(3, 2, 4)
g.add_edge(3, 4, 6)

g.print_graph()
x,y=g.most_outgoing_edge()
print(x,y)



