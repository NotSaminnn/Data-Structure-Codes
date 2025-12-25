class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def calculate_energy(root, destination):
    """
    Calculate the product of node values along the path to the destination in a BST.
    Returns the product if destination exists, otherwise "route does not exist".
    """
    if root is None:
        return "route does not exist"
    
    product = 1
    current = root
    
    while current is not None:
        product *= current.value
        
        if current.value == destination:
            return product
        
        if destination < current.value:
            current = current.left
            calculate_energy(current, destination)
        else:
            current = current.right
            calculate_energy(current, destination)

    
    return "route does not exist"

#Smallest K value

def smallest_sum(root, k):
    def in_order_traversal(node, count, result):
        if node is None or count >= k:
            return
        
        # Traverse left subtree
        in_order_traversal(node.left, count, result)
        
        # Process current node if we still need more nodes
        if count < k:
            result += node.value
            count+= 1
        
        # Traverse right subtree only if needed
        if count < k:
            in_order_traversal(node.right, count, result)

    
    count = 0  # Track how many nodes we've processed
    result = 0  # Accumulate the sum
    in_order_traversal(root, count, result)
    
    return result



#Find value

def calculate_energy(root, destination):
    """
    Calculate the product of node values along the path to the destination in a BST.
    Returns the product if destination exists, otherwise "route does not exist".
    """
    if root is None:
        return "route does not exist"
    
    product = [0]*100
    current = root
    count=0
    
    while current is not None:
        product[count] = current.value
        count += 1

        if current.value == destination:
            return product

        if destination < current.value:
            current = current.left
            calculate_energy(current, destination)
        else:
            current = current.right
            calculate_energy(current, destination)

x=calculate_energy(root, destination)

for i in range(len(x)):
    if x[i]==0:
        break
    print(x[i], end=" ")

product=[10,15,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]