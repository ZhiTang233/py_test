g_num = 10


def func1():
    print(f'func1中{g_num}')


def func2():
    g_num = 20
    print(f'func2中{g_num}')


def func3():
    global g_num  # 这个函数中使用的g_num 都是全局变量,写在函数的第一行
    g_num = 30
    print(f'func3中{g_num}')


print(g_num)
func1()
func2()
func1()
func3()
func1()
