import numpy as np
# https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort
# a1 = np.array([2, 1, 5, 3, 7, 4, 6, 8])
# np.sort(a1) # 原来的数组没有变化
# print(a1)

""" 
[         第1轴 
    [11, 4, 5, 3, 2],  
                        # 第 0 轴
    [8, 6, 3, 9, 4]   
]
#! shape() 几个表示几维, 元组中第1个数字并不是表示几维, 注意
"""
a2 = np.array([[11, 4, 5, 3, 2], [8, 6, 3, 9, 4] ]) # shape (2, 5)
print("默认", np.sort(a2)) # 默认按照第1个轴进行排序, 也就是按照第1轴进行排序
print(np.sort(a2, axis=0))

print(np.sort(a2, axis=None)) # 拍平排序

# 按照第0 轴进行排序, 也就是说, 谁小谁在上面
""" 
[[ 8  4  3  3  2]
 [11  6  5  9  4]]
"""
print(np.sort(a2, axis=0))

# 结构化数组
dtype = [('name', 'S10'), ('height', float), ('age', int)]
values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38), ('Galahad', 1.7, 38)]
a3 = np.array(values, dtype=dtype)
print(a3)
""" 
排序前
[(b'Arthur', 1.8, 41) (b'Lancelot', 1.9, 38) (b'Galahad', 1.7, 38)]
排序后
[(b'Galahad', 1.7, 38) (b'Arthur', 1.8, 41) (b'Lancelot', 1.9, 38)]
"""
print(np.sort(a3, order='height'))

print("*" * 80)
b = np.array([5, 6, 7, 8])
a = np.array([1, 2, 3, 4])
#! 注意, 参数要是元组
# c = np.concatenate((a, b)) # 默认按照最后一个轴合并, 并排序
c = np.concatenate((a, b), axis=0) # 默认按照最后一个轴合并, 并排序
print(c)
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
""" 
[
    [1, 2]                          [1, 2]   [5]    [1  2  5]
    [3, 4] +  [5, 6] 不行, 得转置 -> [3, 4] + [6] =  [3, 4, 6]
]
原理上相当于矩阵运算
"""
print(np.concatenate((x, y.T), axis=1))

# 为了从数组中删除元素，使用索引来选择要保留的元素很简单
