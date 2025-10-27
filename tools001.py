def add(a, b):
    return a + b


def func():
    print('我是tools001模块中的func函数')
    

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):
        print(f'{self.name}在快乐玩耍')


if __name__ == '__main__':
    print(add(1, 2))
    print('tools001:', __name__)
