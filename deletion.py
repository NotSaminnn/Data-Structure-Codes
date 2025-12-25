
def deletion(heap):
   if heap is None :
       return None 
   

   max_value = heap[0]
   last_value = heap[-1]
   heap[0] = last_value

   del heap[-1]

   i = 0
   n= len(heap)

   while True:
       left = 2*i+1
       right = 2*i+2
       largest = i

       if left < n and heap[left] > heap[largest]:
           largest = left
       if right < n and heap[right] > heap[largest]:
           largest = right

       if largest != i:
           heap[i], heap[largest] = heap[largest], heap[i]
           i = largest
       else:
           break

   return max_value
        
heap =[60, 50, 45, 30, 15, 20, 40, 10]
value=deletion(heap)
print(value)
        


       


   