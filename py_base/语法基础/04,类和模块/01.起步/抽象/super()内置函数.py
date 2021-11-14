# 内置类方法的子类
class LogginDict(dict):
    def __setitem__(self, k, v):
        print('将 %r 设置为 %r' % (k, v))
        super().__setitem__(k, v)
        
# d: dict = {"a": 1, "b": 2}
d = LogginDict()
print(d.__setitem__("c", 3))