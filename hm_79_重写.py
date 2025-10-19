"""
重写：在子类中定义了和父类中名字相同的方法
原因：父类的方法不能满足子类对象的需求
特点：调用子类字节的方法，不能调用父类中的方法
方式：
    覆盖(父类中功能完全抛弃，
    扩展(父类中功能还调用,只是添加一些新功能

覆盖: 直接在子类
"""


class Dog:
    def bark(self):
        print('叫---')
        print('叫---')


class XTQ(Dog):
    def bark(self):
        print('喜欢叫=--')
        super().bark()
        print('喜欢叫---')


xtq = XTQ()
xtq.bark()
