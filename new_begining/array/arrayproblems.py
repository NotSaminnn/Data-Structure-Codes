import numpy as np 


# #problem-1
# def compress_matrix(mat):

#     row = len(mat)
#     col = len(mat[0])
#     new_row = row//2
#     new_col = col//2

#     new_mat = np.zeros((row//2, col//2),dtype=int)

#     for i in range(0,row,2):
#         for j in range(0,col,2):
#             new_mat[i//2][j//2] = mat[i][j] + mat[i][j+1] + mat[i+1][j] + mat[i+1][j+1]

#     return new_mat


# mat = np.array([[1, 2, 3, 4], 
#                 [5, 6, 7, 8], 
#                 [9, 10, 11, 12], 
#                 [13, 14, 15, 16]])








# #problem-2

# def sum_diff(mat):
#     row = len(mat)
#     col = len(mat[0])


#     sum_col = np.zeros((col,),dtype=int)

#     for i in range(col):
#         for j in range(row):
#             sum_col[i] += mat[j][i]
    
#     diff_mat = np.zeros((col-1,),dtype=int)
#     for i in range(col-1):
#         diff_mat[i] = sum_col[i+1]-sum_col[i]

#     return diff_mat

# mat = np.array([[1, 2, 3, 4], 
#                 [5, 6, 7, 8], 
#                 [9, 10, 11, 12], 
#                 [13, 14, 15, 16]])
# print(sum_diff(mat))    


#problem-3

mat = np.array([[1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [9, 10, 11, 12], 
                [13, 14, 15, 16]])


n = len(mat)        
top = 0
bottom = n-1
left = 0
right = n-1

for i in range(left,right):
    mat[top][i] = mat[top][i+1]

for j in range(top,bottom):
    mat[j][right] = mat[j+1][right]
for k in range(right,left,-1):
    mat[bottom][k] = mat[bottom][k-1]
for l in range(bottom,top+1,-1):
    mat[l][left] = mat[l-1][left]

print(mat)


    
