"""
https://www.bilibili.com/video/BV18E411F7YA?p=2
f(x) = x^2
aList = [1, 2, 3, 4, 5, 6]
"""
aList = [1, 2, 3, 4, 5, 6]

def f(x):
    return x ** 2

result = map(f, aList)

print(list(result))