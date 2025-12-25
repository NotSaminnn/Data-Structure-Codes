class Node:
    def __init__(self, elem=None, next=None):
        self.elem = elem
        self.next = next

class HashTable:
    def __init__(self, length):
        self.ht = [None] * length  # Initialize with None instead of Node objects
        self.length = length

    def show(self):
        count = 0
        for i in self.ht:
            temp = i
            print(count, end=" ")
            while temp != None:
                print(temp.elem, end="-->")
                temp = temp.next
            count += 1
            print()

    def __hash_function(self, key):  
        n = len(key)
        sum = 0

        if n % 2 == 0:
            for i in range(0, n, 2):
                sum += ord(key[i])
        else:
            for i in range(1, n, 2):
                sum += ord(key[i])
        
        x = sum % self.length
        return x
    
    def insert(self, key, value):
        index = self.__hash_function(key)
        newNode = Node((key, value))

        if self.ht[index] is None:
            self.ht[index] = newNode
            return
        
        temp = self.ht[index]

        # Check for duplicate key and update
        while temp is not None:
            if temp.elem[0] == key:  # Check if key already exists
                temp.elem = (key, value)  # Update the value
                return
            temp = temp.next
        
        # Reset temp to head for insertion
        temp = self.ht[index]
        
        # Insert at beginning if new value is greater than head
        if value > temp.elem[1]:
            newNode.next = self.ht[index]
            self.ht[index] = newNode
            return
        
        # Find the correct position to insert (descending order by value)
        while temp.next is not None:
            if value > temp.next.elem[1]:
                newNode.next = temp.next
                temp.next = newNode
                return
            temp = temp.next
        
        # Insert at the end if no suitable position found
        temp.next = newNode

# Driver Code
ht = HashTable(3)
ht.insert("apple", 20)
ht.insert("coconut", 90)
ht.insert("cherry", 50)
ht.show()
print("------------")
ht.insert("banana", 30)
ht.insert("pineapple", 50)
ht.show()
print("------------")
ht.insert("apple", 100)
ht.insert("guava", 10)
ht.show()