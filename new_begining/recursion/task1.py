def task1A():
    i = 1
    while i <11:
        print(i)
        i += 1
# task1A()

def task1B(i=1):
    if i > 10:
        return
    print(i)
    task1B(i+1)

# task1B()

def task1C():
    N = int(input("Enter a number: "))
    i = 1
    while i <= N:
        print(i)
        i += 1

# task1C()

def task1D(N,i=1):
    if i > N:
        return
    print(i)
    task1D(N,i+1)
    
n = int(input("Enter a number: "))
# task1D(n)


def task2A(arr):
    i = 0
    while i < len(arr):
        print(arr[i])
        i += 1

def task2B(arr,i=0):
    if i >= len(arr):
        return
    print(arr[i])
    task2B(arr,i+1)

def task2C(arr):
    sum = 0
    i = 0
    while i < len(arr):
        sum += arr[i]
        i += 1
    print("Sum is:",sum)

def task2D(arr,i=0,sum=0):
    if i >= len(arr):
        print("Sum is:",sum)
        return
    sum += arr[i]
    task2D(arr,i+1,sum)
def task2DV2(arr , i=0):
    if i >= len(arr):
        return 0
    return arr[i] + task2DV2(arr,i+1)


arr = [1,2,3,4,5]

