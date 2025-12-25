class Node:
  def __init__(self,elem):
    self.elem = elem
    self.left = None
    self.right = None


def insert(root,elem):
   if root is None:
         return Node(elem)
   if elem < root.elem:
         root.left = insert(root.left,elem)
   else:
         root.right = insert(root.right,elem)
   return root


arr = [4,2,6,1,3,5,7]
root = Node(arr[0])
for i in range(1,len(arr)):
    root = insert(root,arr[i])



def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.elem,end=" ")
        inorder(root.right)


def delete(root, elem):
    # Base case: empty tree
    if root is None:
        return root
    
    # Traverse the tree to find the node to delete
    if elem < root.elem:
        root.left = delete(root.left, elem)
    elif elem > root.elem:
        root.right = delete(root.right, elem)
    else:
        # Node found! Now handle deletion cases
        
        # Case 1: Node has no children (leaf node)
        if root.left is None and root.right is None:
            return None
        
        # Case 2: Node has only right child
        if root.left is None:
            return root.right
        
        # Case 3: Node has only left child
        if root.right is None:
            return root.left
        
        # Case 4: Node has both children
        # Find the inorder successor (smallest node in right subtree)
        successor = find_min(root.right)
        
        # Replace root's value with successor's value
        root.elem = successor.elem
        
        # Delete the successor
        root.right = delete(root.right, successor.elem)
    
    return root


def find_min(root):
    """Helper function to find the minimum node in a subtree"""
    current = root
    while current.left is not None:
        current = current.left
    return current


inorder(root)


def find_right_min(root):
    while root.left is not None:
        root = root.left
    return root

def deletation(root,val):
    if root is None:
        return None
    


    if val < root.elem:
        root.left = deletation(root.left,val)
    
    elif val > root.elem:
        root.right = deletation(root.right,val)

    else:

        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        if root.left is None and root.right is None:
            return None
    

    successor = find_right_min(root.right)
    root.elem = successor.elem
    root.right = deletation(root.right,successor.elem)

    return root


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def count_nodesV2(root,sum):
    if root is None:
        return sum
    
    sum += 1

    sum = count_nodesV2(root.left,sum)
    sum = count_nodesV2(root.right,sum)
    
    return sum


def print_kth_level(root,k):

    if root is None:
        return
    if k == 0:
        print(root.elem,end=" ")
        return
    print_kth_level(root.left,k-1)
    print_kth_level(root.right,k-1)





