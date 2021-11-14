
class Student:
    def __init__(self, name: str, age: int)-> None:
        self.name = name
        self.age = age
    def get_name(self)-> str:
        return self.name
        
    def get_age(self)->int: 
        return self.age


s = Student('westes', 10)

# 有没有这个属性
# print(hasattr(s, "name"))
# print(hasattr(s, "get_name"))
# print(hasattr(s, "set_name"))
# print(getattr(s, "get_name"))
print("获取对象的属性和方法---> ")
print(dir(s))
print("*" * 120)
print("获取类时只能得到方法---> ")
print(dir(Student))

