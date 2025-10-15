"""
# 从函数的语法上讲，self是形参 就可以是任意的变量名
self是普通的形参，但是在调用的时候没有传递实参值
python解释器在执行代码的时候，自动将调用这个方法的对象 传递给了self
即self的本质是对象

验证：只需要确定通过哪个对象调用 对象的引用和self的引用是一样的
self是函数中的局部变量，直接创建的对象时全局变量
"""


class Cat:
    def eat(self):
        print(f'{id(self)}, self')
        print('小猫爱吃鱼')


# 创建对象
blue_cat = Cat()
print(f'{id(blue_cat)}, blue_cat')
blue_cat.eat()  # blue_cat对象调用eat方法，解释器就将blue_cat对象传给self
print("-" * 30)
# 创建对象
black_cat = Cat()
print(f'{id(black_cat)}, block_cat')
black_cat.eat()
