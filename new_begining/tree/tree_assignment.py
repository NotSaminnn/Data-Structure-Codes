class Node:
  def __init__(self,elem):
    self.elem = elem
    self.left = None
    self.right = None


#Task-5
def sumof_tree(root):
    if root is None:
        return 0
    return root.elem + sumof_tree(root.left) + sumof_tree(root.right)

def substract_summation(root):
   
   left_sum = sumof_tree(root.left)
   right_sum = sumof_tree(root.right)
   return left_sum - right_sum



#Task-4
class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None
def preOrder(root):
  if root == None:
    return

  print(root.elem, end = ' ')
  preOrder(root.left)
  preOrder(root.right)

def tree_construction(arr, i = 1):
  if i>=len(arr) or arr[i] == None:
    return None
  p = BTNode(arr[i])
  p.left = tree_construction(arr, 2*i)
  p.right = tree_construction(arr, 2*i+1)
  return p


root2 = tree_construction([None, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', None, None, None, 'I', 'J', None, 'k'])
preOrder(root2)



def swap_child(root,level,M):
  if root == None:
    return None
  
  if level < M:
    root.left, root.right = root.right, root.left
  
  swap_child(root.left,level+1,M)
  swap_child(root.right,level+1,M)

  return root
#Driver Code
root=BTNode('A')
#Write other nodes by yourself from the given tree of Doc File, take idea of creating the tree from task6.


print('Given Tree Inorder Traversal: ', end = ' ')
preOrder(root)   #Given Tree Inorder Traversal: G D H B I E A C J F
print()

root2 = swap_child(root, 0, 2)
print('Swapped Tree Inorder Traversal: ', end = ' ')
preOrder(root2)  #Swapped Tree Inorder Traversal: J F C A I E B G D H

#Task-6

def dif_of_lvlsum(root,level,value =0):
  if root == None:
    return None
  

  if level %2==0:
    value += root.elem
  else:
    value -= root.elem

  dif_of_lvlsum(root.left,level+1,value)
  dif_of_lvlsum(root.right,level+1,value)

  return value
  
def dif_of_lvlsumV2(root,level):
    if root == None:
        return 0
    
    if level %2==0:
        return root.elem + dif_of_lvlsumV2(root.left,level+1) + dif_of_lvlsumV2(root.right,level+1)
    else:
        return -root.elem + dif_of_lvlsumV2(root.left,level+1) + dif_of_lvlsumV2(root.right,level+1)

