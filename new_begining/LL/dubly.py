#Task-1

import numpy as np
class Node:
  def __init__(self, elem):
    self.elem = elem
    self.next = None

def createDummyHeadedSinglyCircularLL(values, circular=False):
    dHead = Node(None)
    n = dHead
    for val in values:
        new_node = Node(val)
        n.next = new_node
        n = new_node
    # Make it circular
    if circular:
        n.next = dHead
    return dHead

def printDummyHeadedSinglyCircularLL(head):
    print("[X]", end = ' --> ')
    n = head.next
    while n != head:
        print(f'[{n.elem}]', end = ' --> ')
        n = n.next
    print("(back to start)")


def sumOddAppend(dhead):
    temp = dhead.next
    prev = dhead  # This will track the previous node
    sum_odd = 0
    
    # First pass: remove odd nodes and sum their values
    while temp != dhead:
        if temp.elem % 2 != 0:
            # Add to sum and remove the node
            sum_odd += temp.elem
            prev.next = temp.next
            temp = temp.next
        else:
            # Move both pointers forward
            prev = temp
            temp = temp.next
    
    # Find the last node
    last = dhead
    while last.next != dhead:
        last = last.next
    
    # Create only one new node with the sum and append it
    newNode = Node(sum_odd)
    last.next = newNode
    newNode.next = dhead
    
    return dhead


# x= createDummyHeadedSinglyCircularLL([1,2,3,4,5,6,7,8,9], circular=True)
# y= sumOddAppend(x)
# printDummyHeadedSinglyCircularLL(y)


    
#Task-2


class DNode:
  def __init__(self, elem):
    self.elem = elem
    self.next = None
    self.prev = None


def createDummyHeadedDoublyLL(values, circular=False):
    dHead = DNode(None)
    n = dHead
    # Create and link all value nodes
    for val in values:
        new_node = DNode(val)
        n.next = new_node
        new_node.prev = n
        n = new_node
    if circular:
        n.next = dHead
        dHead.prev = n
    return dHead

def printDummyHeadedDoublyCircularLL(head):
    print("Forward: ",end="")
    print("[X]", end = ' --> ')
    n = head.next
    lstNode = None
    while n != head:
        if n==None :
            print("\n[ERROR!!] NOT CIRCULAR!!!")
            return
        print(f'[{n.elem}]', end = ' --> ')
        n = n.next
    print("(back to start)")
    print("Backward: ",end="")
    n = head.prev
    if n==None:
        print("[ERROR!!] No PREV Connecion from HEAD")
        return
    while n != head:
        print(f'[{n.elem}]', end = ' --> ')
        n = n.prev
    print("[X] --> (back to end)\n")



def rangeMove( dhead, start, end ):
    temp = dhead.next
    temp2 = dhead

    tail = dhead
    while tail.next != dhead:
        tail = tail.next
    main_tail = tail

    while temp != None and temp != main_tail.next:
        if start <= temp.elem <= end:
            x= temp
            temp2.next = temp.next
            tail.next = x
            x.next = None
            tail = x
            temp = temp2.next
        else:
            temp2 = temp
            temp = temp.next


x= createDummyHeadedDoublyLL([5,3,7,1,9,6,2,4], circular=True)
rangeMove(x,5,7)
printDummyHeadedDoublyCircularLL(x)






    
    



