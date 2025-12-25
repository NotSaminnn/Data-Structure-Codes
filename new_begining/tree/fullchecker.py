def full_or_no(root):
    if root is None:
        return True
    
    if root.left is None and root.right is None:

        return True
    
    if root.left is not None and root.right is not None:
        return full_or_no(root.left) and full_or_no(root.right)

    return False


def full_or_noV2(root):
    if root is None:
        return True
    if root.left is None and root.right is not None:
        return False
    if root.right is not None and root.left is None:
        return False
    
    if not full_or_noV2(root.left):
        return False
    if not full_or_noV2(root.right):
        return False
    return True 