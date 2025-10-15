"""
添加属性
对象.属性名 = 属性值

类内部添加
在内部方法中，self是对象
self.属性名 = 属性值
在类中添加属性一般写作__init__方法中

类外部添加
对象.属性名 = 属性值 # 一般不使用


获取属性
对象.属性名

类内部
 在内部方法中，self是对象
 self.属性名

 类外部
 对象.属性名 # 一般很少使用

"""


class Cat:
    def eat(self):
        print(f'小猫是{self.name}今年{self.age}岁，爱吃鱼')


blue_cat = Cat()
blue_cat.name = '蓝猫'
blue_cat.age = 2
blue_cat.eat()
print('-' * 30)
black_cat = Cat()
black_cat.name = '黑猫'
black_cat.age = 2
black_cat.eat()
