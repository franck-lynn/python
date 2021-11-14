from sympy import *
# https://docs.sympy.org/latest/tutorial/basic_operations.html
# 定义未知数
x, y, z = symbols("x y z")

expr1 = cos(x) + 1
# 把 x 替换成 y
expr2 = expr1.subs(x, y)
print(expr2)

print(expr1.subs(x, 0))

print("*" * 80)

print((x**y).subs(y, x**x) )

print("*" * 80)

# 把字符串转成 sympy 表达式
str_expr = "x ** 2 + 3 * x - 1/2"
expr = sympify(str_expr) 
print(expr.subs(x, 2))

expr = sqrt(8)
print(expr, expr.evalf())

print("*" * 80)
# 把表达式转换成函数
import numpy as np
a = np.arange(10)
# lambdify 实际上是转成了一个函数
f = lambdify(x, sin(x), 'numpy')
print(f(a))







