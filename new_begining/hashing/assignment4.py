class Node_pair:
    def __init__(self, key, value, next=None):
        self.key, self.value, self.next = key, value, next


class Hashtable:
    def __init__(self, size):
        self.ht = [None] * size
        self.length = size  # Add this to store the table size


    def insert(self, s):
        hashed_index = self.__hash_function(s[0])
        pair = Node_pair(s[0], s[1])
        if self.ht[hashed_index] is None:
            self.ht[hashed_index] = pair
        else:
            pair.next = self.ht[hashed_index]
            self.ht[hashed_index] = pair

    def create_from_array(self, arr):
        for i in arr:
            self.insert(i)

    def print_hashtable(self):
        idx = 0
        for i in self.ht:
            print(idx, ':', end=' ')
            head = i
            while head is not None:
                print(f'({head.key}, {head.value})', end='-->')
                head = head.next
            print('None')
            idx += 1

    def __hash_function(self, key):
        return (key + 3) % self.length
    
    
    def remove(self, key):
        index = self.__hash_function(key)
        
        # If the bucket is empty, key doesn't exist
        if self.ht[index] is None:
            return
        
        # If the first node in the bucket has the key
        if self.ht[index].key == key:
            self.ht[index] = self.ht[index].next
            return
        
        # Search for the key in the linked list
        current = self.ht[index]
        while current.next is not None:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next


# Driver Code
arr = [(34, 'Abid'), (4, 'Rafi'), (6, 'Karim'), (3, 'Chitra'), (22, 'Nilu')]
ht = Hashtable(6)
ht.create_from_array(arr)
ht.print_hashtable()

print('======================')

ht.remove(9)
ht.print_hashtable()

print('======================')

ht.remove(4)
ht.print_hashtable()