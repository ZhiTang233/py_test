def func1():
    num = 10
    print(f'func1函数中{num}')


def func2():
    num = 100  # 可以在不同的函数中定义名字相同的局部变量
    print(f'func2函数中{num}')


func1()
func2()
