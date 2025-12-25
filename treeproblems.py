class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# check identical
def identical(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    
    return (root1.value == root2.value) and identical(root1.left, root2.left) and identical(root1.right, root2.right)




#mirror
def mirror(root):
    if root == None:
        root.left,root.right = mirror(root.right),mirror(root.left)

    return root 

#balanced


def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def is_balanced(root):
    if root == None:
        return True
    left_height = height(root.left)
    right_height = height(root.right)


    if abs(left_height - right_height) > 1:

        return False
    return is_balanced(root.left) and is_balanced(root.right)





#sumvalue

def sumvalue(root):
    if root == None:
        return True
    if not root.left and not root.right:
        return root.value
    
    if root.left != None:
        left_value = root.left.value
    else:
        left_value = 0
    if root.right != None:
        right_value = root.right.value
    else:
        right_value = 0

    if root.value == left_value + right_value:
        return sumvalue(root.left) and sumvalue(root.right)
    
    else:
        return False



 #largest value on each level


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def largest_value_each_level(root):
    if root == None:
        return []
    
    # Use a large enough array for the queue
    l = [None] * 10000
    l[0] = root

    start = 0
    end = 1

    result = [None] * 100
    level = 0

    while start < end:
        level_start = start
        level_end = end
        max_value = -99999999

        # Process all nodes at current level
        for i in range(level_start, level_end):
            node = l[i]
            max_value = max(max_value, node.value)
            
            # Add children to the queue
            if node.left:
                l[end] = node.left
                end += 1
            if node.right:
                l[end] = node.right
                end += 1

        result[level] = max_value
        level += 1
        start = level_end  # Move start to beginning of next level

    # Return only the filled portion of result array
    return result[:level]






class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def OddSwap(root):
    level = 0
    if root is None:
        return root
    
    def swap_values(node, current_level):
        if node is None:
            return
        
        if current_level % 2 != 0:
    
            if (node.right is not None and node.left is not None and 
                node.right.value > node.left.value):
                # Swap the values
                node.left.value, node.right.value = node.right.value, node.left.value
                swap_values(node.left, current_level + 1)
                swap_values(node.right, current_level + 1)
            else:
                swap_values(node.left, current_level + 1)
                swap_values(node.right, current_level + 1)
    
    swap_values(root, level)
    return root

def left_energy_signature(root):
    if root is None:
        return 0
    
    total = 0
    
    if root.left is not None and root.right is None:
        if root.left.left is None and root.left.right is None:
            total += root.value
    total += left_energy_signature(root.left)
    total += left_energy_signature(root.right)
    
    return total