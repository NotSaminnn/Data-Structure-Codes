#Task-1 (matrix summation)

import numpy as np


def matrix_sum(arr1, arr2):



    row = len(arr1)
    col = len(arr1[0])

    arr3 = np.zeros((row,col),dtype=int)

    for i in range(row):
        for j in range(col):
            arr3[i][j] = arr1[i][j] + arr2[i][j]
    return arr3


arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[7, 8, 9],
                 [10, 11, 12]])





#Task-2 (Matrix multiplication)


arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],[7,8,9]])

arr2 = np.array([[7, 8, 9],
                 [10, 11, 12],[13,14,15]])



def matrix_multiply(arr1, arr2):

    row1 =len(arr1)
    col1 = len(arr1[0])
    col2 = len(arr2[0])

    multi_mat = np.zeros((row1,col2),dtype=int)

    for i in range(row1):
        for j in range(col2):
            sum = 0
            for k in range(col1):
                sum += arr1[i][k] * arr2[k][j]     # multi_mat = arr1[i][0] * arr2[0][j] + arr1[i][1] * arr2[1][j] + ...
            multi_mat[i][j] = sum
    return multi_mat



#Task-3 (Transpose of a matrix)

def transpose_matrix(arr):

    row = len(arr)
    col = len(arr[0])

    for i in range(col):
        print
        for j in range(i+1,row):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    return arr


arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7,8,9]])

print(transpose_matrix(arr))