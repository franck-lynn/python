import collections
import inspect
import numpy
# https://www.geeksforgeeks.org/inspect-module-in-python/


class A:
    pass


print("是一个类吗? ", inspect.isclass(A))

print("是一个模块吗? ", inspect.ismodule(numpy))


def fun(a):
    return 2 * a
    pass


print("是一个函数吗? ", inspect.isfunction(fun))



print("检查参数是不是一个方法的名字", inspect.ismethod(collections.Counter))

print("*" * 80)
# 检查来源
class A:
    pass

class B(A): 
    pass

class C(B):
    pass

print("类C的来源 ", inspect.getmro(C))

for i in inspect.getclasstree(inspect.getmro(C)):
    print(i)







