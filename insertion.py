def insertion(heap,value):
    heap.append(value)

    i = len(heap) - 1

    while i>0:
        parent = (i-1)//2
        if heap[i] > heap[parent]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent




heap= [0,0,0,0]

insertion(heap,10)

print(heap)
