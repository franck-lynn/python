# https://docs.python.org/zh-cn/3/library/collections.abc.html
from collections.abc import Sequence, Set


class C(Sequence):
    def __init__(self):
        pass

    def __getitem__(self, key):
        pass

    def __len__(self):
        pass

    def count(self, value):
        pass

# 类 C 继承 Sequence


print("C是Sequence子类吗? ", issubclass(C, Sequence))
print("C实例是属于Sequence类吗? ", isinstance(C(), Sequence))

# 注册虚拟主类


class E:
    def __init__(self):
        pass

    def __getitem__(self, key: str):
        pass

    def __len__(self):
        pass

    def count(self, value):
        pass


Sequence.register(E)

print("C是Sequence子类吗? ", issubclass(E, Sequence))
print("C实例是属于Sequence类吗? ", isinstance(E(), Sequence))


class ListBasedSet(Set):
    def __init__(self, iterable):
        # 初始化时, 把元素都加入到数组, 形成 [a, b, c] 这样的结构
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)
                
    def __iter__(self):
        # 可迭代
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

    def __str__(self):
        return str(self.elements)


s1 = ListBasedSet('abcdef')
s2 = ListBasedSet('defghi')

overlap = s1 & s2

print(overlap)
