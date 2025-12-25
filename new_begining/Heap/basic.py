class MinHeap:
    def __init__(self,capacity):
        self.arr = [0]*(capacity)
        self.capacity = capacity
        self.size = 0


    def insert(self,value):
        if self.size == self.capacity:
            return "Heap is full"
        
        self.arr[self.size] = value
        self.swim(self.size)
        self.size += 1

    def swim(self,index):
        while index > 0:

            parent = (index-1)//2

            if self.arr[index] < self.arr[parent]:
                self.arr[index],self.arr[parent] = self.arr[parent],self.arr[index]
                index = parent
    
    def extract_min(self):
        if self.size == 0:
            return "Heap is empty"
        
        val = self.arr[0]
        self.size -= 1
        self.arr[0] = self.arr[self.size]
        self.sink(0)
        return val
    
    def sink(self,index):
        
        while 2*index + 1 < self.size:
            left = 2*index + 1
            right = 2*index + 2
            smallest = index

            if self.arr[left] < self.arr[smallest]:
                smallest = left
            if self.arr[right] < self.arr[smallest]:
                smallest = right        
            if smallest != index:
                self.arr[index],self.arr[smallest] = self.arr[smallest],self.arr[index]
                index = smallest


        












obj1


    






    


    

