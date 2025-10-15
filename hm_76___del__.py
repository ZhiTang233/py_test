# __del__ 方法，对象被删除销毁时，自动调用的
"""
1.调用场景，程序代码运行结束，所有对象都被销毁
2.调用场景，直接使用del删除对象
（如果对象有多个名字（多个对象引用一个对象），需要把所有的对象都删除
"""

class Demo:
    def __init__(self, name):
        print('我是__init__')
        self.name = name

    def __del__(self):
        print(f'{self.name} 没了, 给他处理后事')


# Demo('a')

a = Demo('a')
b = Demo('b')
del a  # 删除销毁 对象,
print('代码运行结束')
