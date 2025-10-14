"""
匿名函数：就是使用lambda关键字定义函数
一般称为使用def关键字定义的函数 标准函数

匿名函数只能书写一行代码
匿名函数的返回值不需要return 一行代码的结果就是返回值
语法：
Lambda 参数：一行代码

匿名函数一般不需要我们主动的调用，一般作为函数的参数使用
1.在定义的时候，将匿名函数的引用保存到一个变量中
变量 = Lambda 参数：一行代码
2.使用变量进行调用
变量()
"""

# 无参无返回值


def func1():
    print('hello world')


func1()
# lambda : print('hello lambda')  # 匿名函数的定义
func11 = lambda: print('hello lambda')
func11()

# 无参有返回值


def func2():
    return 10


print(func2())
func22 = lambda: 10
print(func22)
# 有参无返回值


def my_sum(a, b):
    print(a + b)


my_sum(1, 2)
my_sum11 = lambda a, b: print(a+b)
my_sum11(10, 20)
# 有参有返回值


def func4(a, b):
    return a + b


print(func4(1, 2))
func44 = lambda a, b: a+b
print(func44(10, 20))
