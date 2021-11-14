import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
"""  
[    #0  #1  #2   #3
    [1,  2,  3,   4],  # 0
    [5,  6,  7,   8],  # 1
    [9, 10,  11, 12]   # 2
]
"""
print(a[a > 5])
print(np.nonzero(a > 5))

print( (a > 5) | (a == 5) )
b = np.nonzero(a < 5) # 数组中小于 5 的元素的下标, 是一个二维数组, 
print(list(zip(b[0], b[1])))

