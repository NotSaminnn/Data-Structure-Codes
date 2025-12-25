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

#Task-1
def similarity_check(head1,head2):
  temp1 = head1
  temp2 = head2

  while temp1 != None and temp2 != None:
    if temp1.elem != temp2.elem:
      print("Not Similar")
      return
    temp2=temp2.next
    temp1=temp1.next
  if temp1 !=None  and temp2 == None or temp1 == None and temp2 != None:
    print("Not Similar")
  else:
    print("Similar")

building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue']))




#Task-2
def organizeBooks(head,arr):
  n = len(arr)

  for i in range(n):
    temp =head
    while temp.next != None:
      if arr[i] < arr[i+1]:
        x = arr[i] # why save in temporary variable?
        arr[i] = arr[i+1]
        arr[i+1] = x

        y = temp.elem
        temp.elem = temp.next.elem
        temp.next.elem = y

    temp = temp.next
    return head
  


# books1 = createList(np.array(["Dune", "IT", "Coraline", "Inferno", "Twilight"]))
# popularity1 = np.array([8, 10, 5, 10, 6])



#Task-3

def alternate_merge(head1, head2):
    temp1 = head1
    temp2 = head2
    
    while temp1 is not None and temp2 is not None:
        x = temp1.next
        y = temp2.next
        
        temp1.next = temp2
        if x != None:
            temp2.next = x
        
        temp1 = x
        temp2 = y
    
    return head1
  

    





head1 = createList(np.array([1,3,5,7]))
head2 = createList(np.array([2,4,6,8,10,12]))


#Task -4

def sum(head1,head2,head3):
  temp1 = head1
  temp2 = head2
  temp3 = head3
  while temp3.next != None:
    temp3 = temp3.next

  while temp1 != None:
    sum = 0
    sum += temp1.elem
    sum += temp2.elem
    newNode = Node(sum)
    temp3.next = newNode
    temp3 = temp3.next
    temp1 = temp1.next
    temp2 = temp2.next
    sum = 0
  return head3

head1 = createList(np.array([1,3,5,7]))
head2 = createList(np.array([2,4,6,8]))
head3 = createList(np.array([9,9,9]))

# z = sum(head1,head2,head3)
# printLinkedList(z)




#practice problems from LL


# if a given linked list has  integers m and n and the linked list would remove all of the lists between m to n and generate Output. here in the input indexing starts from 1
# input 1->2->3->4->5->6->7->8 
# m=3, n=7
#  output: 1-> 5


def removeMN(head, m, n):
    temp = head
    header = None
    tail = None

    position = 1
    while temp != None:
        if position == m - 1:  # We found the node before m
            header = temp
        temp = temp.next
        position += 1
    
    # Find the node at position n (to get tail as n.next)
    temp = head
    position = 1
    while temp != None:
        if position == n: 
            tail = temp.next
        temp = temp.next
        position += 1 

    header.next = tail
    
    return head


head = createList(np.array([1,2,3,4,5,6,7,8]))
head = removeMN(head,3,7)

printLinkedList(head)


      










