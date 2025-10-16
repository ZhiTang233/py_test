"""
类名 Student
属性 姓名 name 年龄 age
方法 吃饭eat
     睡觉sleep
     过年year

"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}要吃饭')

    def sleep(self):
        print(f'{self.name}要睡觉')

    def year(self):
        self.age += 1

    def __str__(self):
        return f'{self.name}, {self.age}岁'


xm = Student('小明', 18)
print(xm)
xm.eat()
xm.sleep()
xh = Student('小红', 17)
print(xh)
xh.eat()
xh.sleep()
