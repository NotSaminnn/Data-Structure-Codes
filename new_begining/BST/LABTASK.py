#Task-4
def rangeSum(root,low,high):
    if root is None:
        return 0
    
    sum = 0
    if low <= root.elem <= high:
        sum += root.elem

    if root.elem > low:
        sum += rangeSum(root.left,low,high)
    if root.elem < high:
        sum += rangeSum(root.right,low,high)
    
    return sum

    
def rangeSumV2(root,low,high,sum=0):
    if root is None:
        return 0
    
    if low <= root.elem <= high:
        sum += root.elem


    return sum + rangeSumV2(root.left,low,high,sum) + rangeSumV2(root.right,low,high,sum)


    

#Task-5
def mirrorSum(root):
    return sumChecker(root.left,root.right)

def sumChecker(left,right):

    if left is None or right is None:
        return 0
    
    total = left.elem + right.elem

    total += sumChecker(left.left,right.right)
    total += sumChecker(left.right,right.left)


def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    if left_height > right_height:
        return 1 + left_height
    else:
        return 1 + right_height
    
    
    return 1 + max(height(root.left),height(root.right))
    
