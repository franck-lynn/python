
import numpy as np

a1 = np.array([1, 2, 3, 4, 5, 6])

""" 
原来一维数组 6个元素
[1, 2, 3, 4, 5, 6]
# 二维数组, 
[     
           第1轴
    [1, 2, 3, 4, 5, 6] 第0轴
]
"""
a2 = a1[np.newaxis, :]
print(a2)



a3 = a1[:, np.newaxis]
print(a3)
