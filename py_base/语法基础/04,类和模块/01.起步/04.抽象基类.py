# https://www.bilibili.com/video/BV1Cq4y1Q7Qv?p=13&spm_id_from=pageDriver
# 抽象基类 abc 不能实例化
# 检查某个类是否有某种方法
import abc
from collections.abc import Sized


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(["bobby1", "bobby2"])
# hasattr() 是否有 len 这个属性
print(hasattr(com, '__len__'))
print(len(com))
# 起到 hasattr() 一样的效果
# 相当于接口
print(isinstance(com, Sized))
""" 
# 我们需要强制某个子类必须实现某些方法
# 实现了一个 web 框架, 集成 cache(redis, cache, memoryCache)
# 需要设计一个基类, 值得子类必须实现某些方法
class ImoocWeb:
    def get_url(self, key):
        pass
    def set_url(self, key, value):
        pass
"""
# 模拟实现一个抽象基类


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    def set(self, key, value):
        pass


# 要实现抽象基类中定义的方法, 强制实现抽象基类定义的方法
class RedisCache(CacheBase):
    def get(self, key):
        pass

    def set(self, key, value):
        pass


redis_cache = RedisCache()
redis_cache.set('key', "value")
