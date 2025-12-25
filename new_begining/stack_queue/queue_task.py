# YOU MUST RUN THIS CELL
# BUT DO NOT modify the CODE in this cell
class Node:
  def __init__(self,elem=None,next=None):
    self.elem = elem
    self.next = next
class LinkedListQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, elem):
        new_node = Node(elem)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        removed_elem = self.front.elem
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_elem

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        return self.front.elem

    def is_empty(self):
        return self.front is None

    def display_queue(self):
        print("Queue (front to rear):", end=" ")
        current = self.front
        while current:
            print(f"{current.elem} ->", end=" ")
            current = current.next
        print("NULL")



class CallQueue:
    def __init__(self):
        self.vip_queue = LinkedListQueue()
        self.regular_queue = LinkedListQueue()

    def enqueue_call(self, customer_id, is_vip):
        if is_vip == True:
            self.vip_queue.enqueue(customer_id)
            print(f"Customer {customer_id}  added to the VIP queue.")
        else:
            self.regular_queue.enqueue(customer_id)
            print(f"Customer {customer_id}  added to the regular queue.")
            

    def dequeue_call(self):
        if not self.vip_queue.is_empty():
            x = self.vip_queue.dequeue()
            print(f"Processing VIP customer {x}.")
        elif not self.regular_queue.is_empty():
            y = self.regular_queue.dequeue()
            print(f"Processing regular customer {y}.")
        else:
            print("No calls in the queue.")
        
        

    def display_queue(self):
        print("VIP Queue:")
        self.vip_queue.display_queue()
        print("Regular Queue:")
        self.regular_queue.display_queue()



# call_center = CallQueue()
# # Enqueueing customers
# call_center.enqueue_call(101, False)  # Regular customer
# call_center.enqueue_call(201, True)   # VIP customer
# call_center.enqueue_call(102, False)  # Regular customer
# call_center.enqueue_call(202, True)   # VIP customer
# call_center.enqueue_call(103, False)  # Regular customer

# call_center.display_queue()

# # Processing calls
# call_center.dequeue_call()
# call_center.dequeue_call()
# call_center.dequeue_call()
# call_center.dequeue_call()
# call_center.dequeue_call()
# call_center.dequeue_call()  # No more calls

# call_center.display_queue()


#Task-2(Assignment)

def removeConsecutiveDups(s):
    temp = LinkedListQueue()

    for i in s:
        temp.enqueue(i)
    
    output = ''

    prev = None
    while not temp.is_empty():    #aaabbaa
        x = temp.dequeue()
        if x !=prev:
            output += x
        prev = x

    return output
    


s= "aaabbaa"
print(removeConsecutiveDups(s))  # aba
