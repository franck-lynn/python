class Animal:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hi, this is ', self.name)

        
# 继承  
class Dog(Animal):

    def greet(self):
        print('wangwang..., Hi, this is ', self.name)

    def run(self):
        print("running...")
        
        
class Cat(Animal):
    def greet(self):
        print('miaomiao..., Hi, this is ', self.name)        
     
def hello(animal):
    animal.greet()   
    
    
dog = Dog('dog')
hello(dog)   
cat = Cat('cat')
hello(cat)
