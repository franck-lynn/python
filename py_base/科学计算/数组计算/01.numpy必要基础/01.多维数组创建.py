# from numpy import ndarray, arange
import numpy as np

a1 = np.arange(6) # [0 1 2 3 4 5] 列表, 类型是一个 ndarray
print(type(a1), a1.shape)

a2 = a1[np.newaxis, :] 
print(a2.shape) 

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(type(a), a.shape)
print(a[0])
print(np.zeros(2))
print(np.empty(2))


# 总数 5 个, (10-0)/ (num -1) 
print(np.linspace(0, 10, num=5))
# 总数 5 个, (10-1)/ (num -1) 9 /4 = 2.25
print(np.linspace(1, 10, num=5))
# 指定数据类型

x = np.ones(2, dtype=np.int64)
print(x)
