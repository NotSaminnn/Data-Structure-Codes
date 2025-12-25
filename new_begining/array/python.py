import numpy as np 

arr = np.array([1,2,3,4,5]) #array has a fixed size and data type alwaysss

for i in range(len(arr)):
    if i %2 != 0:
        print(arr[i])