import numpy as np

#Task-1 (Rotate the matrix downwards by one position)
def row_rotation(arr,week):
    for i in range(week-1):
        arr=rotate_down(arr)
    return arr


def rotate_down(arr):
    row=len(arr)
    col=len(arr[0])

    for j in range(col):
        temp=arr[row-1][j]
        for i in range(row-1,0,-1):
            arr[i][j]=arr[i-1][j]
        arr[0][j]=temp


    return arr




seat_status = np.array([[ 'A' , 'B' , 'C' , 'D' , 'E'],
                  ['F' , 'G' , 'H' , 'I' , 'J'],
                  ['K' , 'L' , 'M' , 'N' , 'O'],
                  ['P' , 'Q' , 'R' , 'S' , 'T'],
                  ['U' , 'V' , 'W' , 'X' , 'Y'],
                  ['Z' , 'AA' , 'BB' , 'CC' , 'DD']])
exam_week=3




#Task-3

def play_game(arr):
    row = len(arr)
    col = len(arr[0])
    sum = 0
    for i in range(row):
        for j in range(col):
            if arr[i][j] % 50 == 0 and arr[i][j] != 0:  # Fixed: check arr[i][j] not arr[i][i]
                # Check all four adjacent cells
                if i-1 >= 0 and arr[i-1][j] == 2:  # Check above
                    sum += 2
                if i+1 < row and arr[i+1][j] == 2:  # Check below
                    sum += 2
                if j-1 >= 0 and arr[i][j-1] == 2:  # Check left
                    sum += 2
                if j+1 < col and arr[i][j+1] == 2:  # Check right
                    sum += 2
    return sum

arena=np.array([[0,2,2,0],
                [50,1,2,0],
                [2,2,2,0],
                [1,100,2,0]
                ])




#Task-4


import numpy as np

def rotate_secret(arr):
    n = len(arr)
    layers = n // 2

    def rotate_layer_once(l):
        top, left = l, l
        bottom, right = n - 1 - l, n - 1 - l
        if top >= bottom or left >= right:
            return
        prev = arr[top + 1][left]
        for j in range(left, right + 1):
            arr[top][j], prev = prev, arr[top][j]
        for i in range(top + 1, bottom + 1):
            arr[i][right], prev = prev, arr[i][right]
        for j in range(right - 1, left - 1, -1):
            arr[bottom][j], prev = prev, arr[bottom][j]
        for i in range(bottom - 1, top, -1):
            arr[i][left], prev = prev, arr[i][left]

    for l in range(layers - 1, -1, -1):
        times = layers - l
        for _ in range(times):
            rotate_layer_once(l)

    for i in range(n):
        for j in range(n):
            print(arr[i][j], end='')
    print()
    return arr

# sample run
board=np.array([
    ['O','R','I','R','N','P'],
    ['G','S','A','A','L','R'],
    ['L','M','N','O','N','Y'],
    ['A','H','U','O','O','P'],
    ['T','F','C','T','H','S'],
    ['E','D','Y','O','C','K']
])
print(rotate_secret(board)  )


