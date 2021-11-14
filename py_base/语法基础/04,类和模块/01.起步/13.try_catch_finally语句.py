def exec_try():
    try:
        print("code start")
        raise KeyError
        return 1
    except KeyError as e:
        print("key error", e)
        return 2
    else:
        print("other error")
        return 3
    finally:
        print("finally")
        # return 4


# 上下文管理器
# with
class Sample:
    # 获取资源
    def __enter__(self):
        return self
    # 释放资源
    def __exit__(self, exc_type, exc_value, trace):
        print("exit", exc_type, exc_value, trace)

    def do_something(self):
        print("do something")


with Sample() as sample:
    sample.do_something()
    
    
# if __name__ == "__main__":
#     result = exec_try()
#     print("result = ", result)
