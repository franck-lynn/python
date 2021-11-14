# 通过一定的机制查询到对象的内部结构
class Date:
    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 实例方法
    def tomorrow(self):
        self.day += 1

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

    # 定义一个静态方法
    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))  # 硬编码 Date

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if(int(year) > 0 and int(month) <= 12 and int(day) > 0 and int(day) <= 31):
            return True
        else:
            return False

    @classmethod  # ! 类方法
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))  # 取消了编码 Date

class Person: 
    name = "users"

class Student(Person):
    def __init__(self,school_name):
        self.school_name = school_name


if __name__ == "__main__":
    user = Student("慕课网")
    # 通过 __dict__ 查询属性, name 属于 Person 这个类,  查询 user.name 会向上查找
    print(user.__dict__) # 对象的属性  {'school_name': '慕课网'}
    print(Person.__dict__) # 类的属性
    print(user.name)
    user.__dict__["school_attr"] = "北京市"
    # print(user.school_attr) # 可以取出, 但 ide 报警
    print(dir(user))
    
    a = [1, 2]
    # print(dir(a))
    # print(a.__dict__) # list 没有 定义 __dict__, 但 dir() 可以
    
    

