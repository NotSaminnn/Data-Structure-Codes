class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None



def max_path_sum(root):

    if root == None:
        return 0
    
    if root.left == None and root.right == None:
        return root.value
    
    left_sum = max_path_sum(root.left)
    right_sum = max_path_sum(root.right)


    return root.value+ max(left_sum,right_sum)



root=Node(1)
root.left=Node(7)
root.right=Node(2)
root.left.right=Node(6)
root.left.right.left=Node(5)
root.left.right.right=Node(11)
root.right=Node(9)
root.right.right=Node(9)
root.right.right.left=Node(5)


print(max_path_sum(root))


