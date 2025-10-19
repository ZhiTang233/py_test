# 需求：小猫爱吃鱼，喝水，定义不带属性的类
class Cat:
    @staticmethod
    def eat():  # self会自动出现
        print('小猫爱吃鱼')

    @staticmethod
    def drink():
        print('小猫要喝水')


# 2.创建对象
blue_cat = Cat()
#  通过对象调用类中的方法
blue_cat.eat()
blue_cat.drink()

# 创建对象
black_cat = Cat()
black_cat.eat()
black_cat.drink()
