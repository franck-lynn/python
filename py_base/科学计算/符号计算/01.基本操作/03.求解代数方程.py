from sympy import *
x, y, z = symbols("x y z")
# 定义方程 x ^2 = 1
eq = Eq(x**2, 1)
print(eq)
# 解方程
roots = solveset(eq, x)
print(list(roots), type(roots))


print(
    solve(eq, x), type(solve(eq, x))
)

print(
    solve(Eq(x**2 - x, x))
)


print(
    "实数范围内无解---> ",
    solveset(Eq(x**2 + 1, x), domain=S.Reals)
)

print(
    # solveset(Eq(exp(x)), x)
    "方程本身无解---> ",
    solveset(exp(x), x)
)

print(
    # solveset(Eq(exp(x)), x)
    "实数范围内无解---> ",
    solveset(sin(x) - 1, x, domain=S.Reals)
)

print(
    # solveset(Eq(exp(x)), x)
    "实数范围内的解---> ",
    solveset(sin(x) - 1, x, domain=S.Reals)
)
print(
    "实数范围内的解, 为什么是空集? 这里需要将 -> \n" + 
    "1/2有理化为一个分式才可以得到正确的解 -> \n"
    "不知道为什么这样 ---> ",
    solveset(Eq(sin(x), Rational(1/2)), x, domain=S.Reals)
)

# https://docs.sympy.org/latest/tutorial/solvers.html
print(
    "不能求解---> ",
    solveset(Eq(cos(x)-x), x)
)



print(
    "实数范围内的解, 为什么是空集? 这里需要将 -> \n" + 
    "1/2有理化为一个分式才可以得到正确的解 -> \n"
    "不知道为什么这样 ---> ",
    solveset(Eq(sin(x), 3/4), x, domain=S.Reals)
)
