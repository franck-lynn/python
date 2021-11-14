"""  
数学题:
已知弧长 l = 156, 弦长 d = 140, 求半径 R 和夹角 a
方程如下:
cos(a) -1 + d **2 / *2 * R**2 = 0
l -(a * R ) = 0
"""

from scipy.optimize import fsolve
from math import cos


def f(x):
    d = 140
    l = 156
    # print(x[0], type(x[0]))
    a = float(x[0])
    r = float(x[1])
    return [
        cos(a) - 1 + d ** 2 / (2 * r**2),
        l - (a * r)
    ]


result = fsolve(f, [1, 1])
print(result)