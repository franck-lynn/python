from sympy import *

a, b, c, d = symbols('a b c d', real = True)
"""  
a*2 + a = 0
a - b = 0
"""
rs = nonlinsolve([a ** 2 + a, a - b], [a, b])
print(rs)


x, y= symbols('x y')
"""  
x^2 + 1 = 0
y^2+ 1 = 0
"""

print(
    nonlinsolve([x**2 + 1, y**2 + 1], [x, y])
)








