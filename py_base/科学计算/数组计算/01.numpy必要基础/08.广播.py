# https://numpy.org/devdocs/user/absolute_beginners.html
import numpy as np

# 相当于 excel 每个单元格进行运算
data = np.array([1.0, 2.0])
print(data*1.6)

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

print(a.sum())
print(a.min(axis=0))

"""  
[             3列
    [[ 2个  ] [     ]   [    ]]
    [[      ] [     ]   [    ]]
                                       4 行
    [[      ] [     ]   [    ]]
    [[      ] [      ]  [    ]]
]
       每个单元格2个
"""
print(np.ones((4, 3, 2)))

