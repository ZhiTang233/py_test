"""
多态：不同的子类对象调用相同的父类方法
以继承和重写父类方法为前提
是调用方法的技巧，不会影响到类的内部设计

"""


class Person:
    def work(self):
        print('人工作')


class Coder(Person):
    def work(self):
        print('开发的工作写代码')


class Tester(Person):
    def work(self):
        print('测试的工作是测试')


class Company:
    def show_work(self, worker):
        worker.work()


c = Company()
xw = Coder()
xh = Tester()
xb = Person()
c.show_work(xw)
c.show_work(xh)
c.show_work(xb)
