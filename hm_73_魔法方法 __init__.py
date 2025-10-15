"""
py中有一类方法，满足某个条件的情况下，会自动调用，这类方法会称为魔法方法

__init__方法
1.什么情况下自动调用
    创建对象之后会自动调用
2.有什么用，用在哪里
    给对象添加属性的（初始化方法，构造方法
    某些代码，在每次创建对象之后，都要执行，就可以将这行代码卸载__init__方法


"""

"""
猫类 属性name age show_info（输出属性

"""


class Cat:
    def __init__(self):
        self.name = '蓝猫'
        self.age = 2
        # 下方代码只是为了验证方法被调用
        print('我是__init__')

    # 输出属性信息
    def show_info(self):
        print(f'小猫的名字是: {self.name}, 年龄是: {self.age}')


Cat()
blue_cat = Cat()  # 创建对象
blue = blue_cat  # 不是创建对象
blue.show_info()


# 创建黑猫

block_cat = Cat()  # 创建对象
block_cat.show_info()
