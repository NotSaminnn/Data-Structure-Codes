

def build_max_heap(array):
    n = len(array)
    for i in range((n//2)-1, -1, -1):
        heapify(array, n, i)
    return array

def heapify(array, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)
    return array

def insertion(heap,value):
    heap.append(value)

    i = len(heap) - 1

    while i>0:
        parent = (i-1)//2
        if heap[i] > heap[parent]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            break
    return heap



#You are given an array of integers and values of  `x` and `y`. You need to create a new heap consisting of the numbers between xth lowest position and yth lowest position from the array. 
array = [11, 15, 8, 2, 31, 23]
x=2
y=5
heap=[]
for i in range(len(array)):
    if array[x]<= array[i] <= array[y]:
        heap = insertion(heap, array[i])
print(heap)

#In applications like batch task scheduling, it's vital to manage tasks based on their urgency, represented by priority levels where a lower number signifies higher urgency. You are given two arrays: one for task IDs and the other for corresponding priorities. These tasks must be organized using a data structure designed for efficient access to the most urgent tasks. However, only those tasks within a specified priority range, marked by lowPriority and highPriority, should be considered. Tasks falling outside this range should be excluded. 
#[Note: The most urgent tasks have lower priority numbers, so the data structure should focus on retrieving the minimum values within the range to correctly identify and process the highest-priority tasks]
tasks = [101, 102, 103, 104, 105, 106, 107, 108, 109]
priorities = [9, 3, 7, 1, 5, 8, 2, 6, 4]
lowPriority = 3
highPriority = 7
heap2=[]
for i in range(len(priorities)):
    if lowPriority <= priorities[i] <= highPriority:
        heap = insertion(heap2, tasks[i])
print(heap2)