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


dog = Dog('dog')
dog.greet()
dog.run()