def add_edge(mat, i, j):
  
    # Add an edge between two vertices
    mat[i][j] = 1  # Graph is 
    mat[j][i] = 1  # Undirected

def display_matrix(mat):
  
    # Display the adjacency matrix
    for row in mat:
        print(" ".join(map(str, row)))  

# Main function to run the program
if __name__ == "__main__":
    V = 4  # Number of vertices
    mat = [[0] * V for _ in range(V)]  

    # Add edges to the graph
    add_edge(mat, 0, 1)
    add_edge(mat, 0, 2)
    add_edge(mat, 1, 2)
    add_edge(mat, 2, 3)

    # Optionally, initialize matrix directly
    """
    mat = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    """

    # Display adjacency matrix
    print("Adjacency Matrix:")
    display_matrix(mat)


def add_edge(adj, i, j):
    adj[i].append(j)
    adj[j].append(i)  # Undirected

def display_adj_list(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(j, end=" ")
        print()

# Create a graph with 4 vertices and no edges
V = 4
adj = [[] for _ in range(V)]

# Now add edges one by one
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 2)
add_edge(adj, 2, 3)

print("Adjacency List Representation:")
display_adj_list(adj)



graph = [(1,3),(2,3),(0,2),(4,1),(1,2)]


#ADJACENCY LIST
graph = [(1,3),(2,3),(0,2),(4,2),(1,2)]

# Use a dictionary for more flexible node indexing
adj_list = {}

for u, v in graph:
    if u not in adj_list:
        adj_list[u] = []
    if v not in adj_list:
        adj_list[v] = []
    
    adj_list[u].append(v)
    adj_list[v].append(u)  # If the graph is undirected

for i in adj_list:
    print(f"{i}: {adj_list[i]}")
