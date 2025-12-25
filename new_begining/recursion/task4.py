def findMax_recursive(head,max=float('-inf')):
    if head is None:
        return max

    if head.elem > max:
        max = head.elem
    
    return findMax_recursive(head.next, max)

def findmin_recursive(head,max=float('inf')):
    if head is None:
        return max

    if head.elem < max:
        max = head
    
    return findmin_recursive(head.next, max)

def sortLL_recursive( head):

    if head is None:
        return head
    
    minimum = findmin_recursive(head)

    head.elem, minimum.elem = minimum.elem, head.elem

    sortLL_recursive(head.next)
    return head
    
[[1,4]]






