#Task-1
class Node:
  def __init__(self,elem=None,next=None):
    self.elem = elem
    self.next = next
class Stack:
  def __init__(self):
    self.__top = None

  def push(self,elem):
    nn = Node(elem,self.__top)
    self.__top = nn

  def pop(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    e = self.__top
    self.__top = self.__top.next
    return e.elem

  def peek(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    return self.__top.elem

  def isEmpty(self):
    return self.__top == None
  
# YOU MUST RUN THIS CELL
# BUT DO NOT modify the CODE in this cell
def print_stack(st):
  if st.isEmpty():
    return
  p = st.pop()
  print('|',p,end=' ')
  if p<10:
    print(' |')
  else:
    print('|')
  #print('------')
  print_stack(st)
  st.push(p)

def remove_block(stack,n):
  temp = Stack()
  count = 0
  while not stack.isEmpty():
    x = stack.pop()
    if count == n:
      break
    else:
      temp.push(x)
      count += 1
  while not temp.isEmpty():
    y= temp.pop()
    stack.push(y)
  return stack



#summer 25 stack problem 

def separate_even_odd(stack):
  even_stack = Stack()
  odd_stack = Stack()
  
  while not stack.isEmpty():
    x = stack.pop()
    if x % 2 == 0:
      even_stack.push(x)
    else:
      odd_stack.push(x)
  
  while not even_stack.isEmpty():
    y = even_stack.pop()
    stack.push(y)

  while not odd_stack.isEmpty():
    z = odd_stack.pop()
    stack.push(z)