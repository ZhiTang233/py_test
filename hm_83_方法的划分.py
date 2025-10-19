"""
方法的划分
方法，使用def 关键字定义在类中的函数就是方法
实例方法(最常用)
定义:在类中直接定义的方法就是 实例方法
class Demo：
    def func(self):
        pass
  

类方法(会用)
定义: 在方法名字的上面书写@classmethod装饰器
class Demo:
    @classmethod
    def func(cls):  # 参数一般写作cls 表示类对象(即类名)
        pass

静态方法(基本不用)
定义:在方法名字的上面书写@ststicmethod 装饰器
class Demo:
    @staticmethod
    def func():
        pass


"""