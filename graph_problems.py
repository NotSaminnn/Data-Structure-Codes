def wantToReturnStart(graph):
    n = len(graph)
    
    # We'll track if we can reach node 0 from each node
    # Start by checking which nodes can directly reach node 0
    can_reach_zero = [False] * n
    
    # Nodes that have a direct edge to node 0
    for i in range(n):
        if graph[i][0] == 1:
            can_reach_zero[i] = True
    
    # Keep propagating the "can reach zero" information
    # until no more changes occur (similar to a simple BFS)
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if not can_reach_zero[i]:
                # Check if node i can reach any node that can reach zero
                for j in range(n):
                    if graph[i][j] == 1 and can_reach_zero[j]:
                        can_reach_zero[i] = True
                        changed = True
                        break
    
    # Finally, check if node 0 can reach any node that can reach node 0
    for j in range(n):
        if graph[0][j] == 1 and can_reach_zero[j]:
            return True
    
    return False

# Build the adjacency matrix based on the given graph description
# From the description: 0 → 1 → 2 → 3 → 4 → 0
graph = [
    [0, 1, 0, 0, 0],  # Node 0 -> Node 1
    [0, 0, 1, 0, 0],  # Node 1 -> Node 2
    [0, 0, 0, 1, 0],  # Node 2 -> Node 3
    [0, 0, 0, 0, 1],  # Node 3 -> Node 4
    [1, 0, 0, 0, 0]   # Node 4 -> Node 0
]

# Test the function
result = wantToReturnStart(graph)
print(result)  # Should print True