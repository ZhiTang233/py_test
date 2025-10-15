"""
类名：人类 person
属性：姓名 name 体重weight
方法：  跑步 run
        吃东西 eat
        添加属性 __init__
        属性信息 __str__

"""


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'姓名: {self.name}, 体重: {self.weight}Kg'

    def run(self):
        # 减体重 即修改属性
        self.weight -= 0.5

    def eat(self):
        self.weight += 0.5


xm = Person('小明', 75.0)
print(xm)
xm.run()
print(xm)
xm.eat()
print(xm)
