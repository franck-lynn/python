import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
data = np.reshape(a, (2, 3))  # 重塑矩阵
print(a)
print(data)

print(a.reshape((2, 3))) # 重塑矩阵

print(data.T) # 转置
print(np.transpose(data)) # 转置

# 二维数组转置
"""  
[
    [1, 2, 3, 4], 
    [5, 6, 7, 8],      
    [9, 10, 11, 12] 
]
"""
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(np.flip(arr_2d, axis=0))




