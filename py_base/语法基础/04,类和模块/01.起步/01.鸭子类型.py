# 鸭式辩型
class Cat:
    def say(self):
        print("I am a cat")


class Dog:
    def say(self):
        print("I am a dog")


class Duck:
    def say(self):
        print("I am a duck")
        
# animal = Cat
# # 并没有继承任何父类, 
# animal().say()

animal_list = [Cat, Dog, Duck]

# 所有的类型都实现了同一个方法, 不需要继承, 只有相同的方法名
# 就可以实现多态
for animal in animal_list:
    animal().say()
    
    
    
a = ['bobby1', 'bobby2']
b = ['bobby2', 'bobby']
name_tuple = ['bobby2', 'bobby']
name_set = set()
name_set.add("bobby5")
name_set.add("bobby6")
a.extend(name_set) # 隐含调用对象的 iterator 方法
print(a)
