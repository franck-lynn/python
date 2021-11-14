# https://segmentfault.com/a/1190000021970821
#! 2.1 __new__
# 在对象实例化过程中最先调用的方法是__new__,
# 该方法接收参数为类，然后将其他参数，传递给__init__,
# 该魔法函数比较少见，可以使用其，创建单例类; __new__方法是一个类方法，
# 需要携带的第一个参数是类
class T1:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        print('1. 创建对象时 时先调用的是 __new__ 魔法函数')
        if cls not in cls._instances:
            cls._instances[cls] = super(T1, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

    def __init__(self, *args, **kwargs):
        print('2. 再调用 __init__ 函数')
        pass
#! 2.2 __init__
# __init__是一个实例方法，用于将构造的实例初始化，在类定义中十分常见
#! 2.3 __del__


if __name__ == "__main__":
    T1()
