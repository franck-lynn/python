import contextlib

# 装饰器可以将函数变成上下文管理器, 类似 try catch finally
@contextlib.contextmanager
def file_open(filename):
    # 获取资源
    print("1. file open", filename)
    yield {}
    # 释放资源
    print("3. file end", filename)
    
with file_open("bobby.txt") as f_opened:
    # 执行资源
    print("2. file processing")    
