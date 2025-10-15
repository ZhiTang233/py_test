"""
__str__方法
1.什么情况下自动调用
    使用print打印对象的时候会自动调用
2.有什么用 用在哪里
    在这个方法中一般书写对象的属性信息的，即打印对象的时候想要查看什么信息 在这个方法中进行定义的
    如果类中没有定义__str__方法，print对象 默认输出对象的引用地址
3.书写的注意事项
    这个方法必须返回 一个字符串
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'小猫的名字: {self.name}, 年龄是: {self.age}')

    def __str__(self):
        # 方法必须返回一个字符串， 只要是字符串就行
        return f'小猫的名字: {self.name}, 年龄是: {self.age}'


blue_cat = Cat('蓝猫', 2)
print(blue_cat)
blue_cat.show_info()

block_cat = Cat('黑猫', 3)
print(block_cat)
block_cat.show_info()
