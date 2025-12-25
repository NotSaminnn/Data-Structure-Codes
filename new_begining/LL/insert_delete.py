import numpy as np
class Node:
  def __init__(self,elem,next = None):
    self.elem,self.next = elem,next

def createList(arr):
  head = Node(arr[0])
  tail = head
  for i in range(1,len(arr)):
    newNode = Node(arr[i])
    tail.next = newNode
    tail = newNode
  return head

def printLinkedList(head):
  temp = head
  while temp != None:
    if temp.next != None:
      print(temp.elem, end = '-->')
    else:
      print(temp.elem)
    temp = temp.next
  print()

def insertion(head,elem,pos=None):
  newNode = Node(elem)

  # Inserting at head
  if pos == 0:
    newNode.next = head
    return newNode
  
  elif pos > 0: #inserting at given position
    temp = head
    count = 0
    while temp != None:
      if count == pos-1:
        newNode.next = temp.next
        temp.next = newNode
        return head
  elif pos is None: # inserting at end
    temp = head
    newNode = Node(elem)
    while temp.next != None:
      temp = temp.next
    temp.next = newNode
    return head
  


def deletion(head,pos=None):
  if pos == 0: # deleting head
    head = head.next
    return head
  
  if pos > 0: # deleting at given position
    temp = head
    count = 0
    while temp != None:
      if count == pos-1:
        temp.next = temp.next.next
        return head

  if pos is None:   # deleting at end
    temp = head
    while temp.next.next != None:
      temp = temp.next
    temp.next = None
    return head


def reverse(head):
    prev = None
    curr = head
    
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head
  





      



    


  



head = createList(np.array([5,10,15,20,25]))

head= insertion(head,2)
printLinkedList(head)

