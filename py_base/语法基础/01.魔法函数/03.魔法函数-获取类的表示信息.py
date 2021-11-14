# https://segmentfault.com/a/1190000021970821
# 4.1 __str__
# 自定义对类调用str()方法时候的行为
# 4.2 __repr__
# 定义对类的实例调用repr()时候的行为，str()和repr()的不同之处是：
# 目标受众的不同，repr()的目的是生成主要是机器可读的输出，许多情况下，
# 可能输出为python代码， 而str()一般输出为人类可读的信息
from sys import getsizeof
from typing import Iterable


class T1:
    def __str__(self):
        return "人可读的信息"

    def __repr__(self):
        return "机器可读的信息"


t1 = T1()
# 输出类的信息
print(t1)
print(repr(t1))


# 4.6 __nonzero__
# 定义对类的实例调用bool()时候的行为，返回值为True或者False，取决于具体的类
class T2:
    def __nonzero__(self) -> bool:
        print("非空")
        return True
        
    def __dir__(self) -> Iterable[str]:
        print("dir调用")
        return ["返回属性列表"]
        
    def __sizeof__(self) -> int:
        # 返回对象的大小
        return 0

t2 = T2()
print(bool(t2))
dir(t2)
print(getsizeof(t2))
