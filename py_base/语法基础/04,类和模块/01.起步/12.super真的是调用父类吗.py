class A: 
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()  # 调用了父类的初始化方法
        

# 既然重写了B的构造函数, 为什么还要去调用 super?

from threading import Thread
class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        super().__init__(name=name) # 这就是一种应用场景, Thread 里有很多应用逻辑就不用再写了


# super() 到底执行顺序是什么样子的? 调用的是 MRO 顺序上的那个类
if __name__ == "__main__":
    b = B()