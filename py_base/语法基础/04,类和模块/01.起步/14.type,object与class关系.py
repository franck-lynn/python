# https://www.bilibili.com/video/BV1Cq4y1Q7Qv?p=4

# type => int => 1
# type => class=> obj
# Object 是最顶层的基类, type 本身也是一个类, 同时也是一个对象, 父类是 Object

print(type.__bases__) # (<class 'object'>,)
print(object.__bases__) # 是空
# object 是 type 的一个实例, type 创建了所有的对象, 包括 object
#  type 继承了 object, type 也是自身的一个实例, 
