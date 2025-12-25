def heap_pop(heap):
    if len(heap) == 0:
        return None
    
    min_value = heap[0]
    last_value = heap[-1]
    heap[0] = last_value
    del heap[-1]
    
    i = 0
    n = len(heap)
    
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        
        if left < n and heap[left] < heap[smallest]:
            smallest = left
        if right < n and heap[right] < heap[smallest]:
            smallest = right
        
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
        else:
            break
    
    return min_value

def insertion(heap, value):
    heap.append(value)
    i = len(heap) - 1
    
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] < heap[parent]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            break

def machine_task(tasks, m):
    heap = []
    for i in range(m):
        insertion(heap, 0)
    
    for task_time in tasks:
        smallest = heap_pop(heap)
        new_value = smallest + task_time
        insertion(heap, new_value)
    
    return heap

task = [2, 4, 7, 1, 6]