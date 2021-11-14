
# import sys
# import os
# sys.path.append(os.path.abspath('.') )
# print(sys.path)

from fibonacci import fib, fib2
# !一般而言, 不建议如下的导入
# !from fibonacci import *, 会导入一批未知的名称
# !import fibonacci as fibo, 这样导入也是可以的
# !from fibonacci import fib as fibo 也是可以的
# import fibonacci
fib(1000)
# fibonacci.fibo(1000)

print(fib2(1000))

