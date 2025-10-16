"""
1.继承描述的是类与类之间的关系
2.继承的好处：减少代码的冗余
继承后，子类可以直接使用父类中定义的公有属性和方法
Object类最顶级的类
"""


class Animal:
    def eat(self):
        print('要吃东西')


class Dog(Animal):
    def bark(self):
        print('叫-----')


class XTQ(Dog):
    pass


ani = Animal()
ani.eat()

dog = Dog()
dog.eat()
dog.bark()

xtq = XTQ()
xtq.bark()
xtq.eat()
