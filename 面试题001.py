def func(list1):
    list1 = [2, 1]  # list1变量的引用发生了改变


my_list = [1, 2]
func(my_list)
print(my_list)


def func1(list1):
    list1[0] = 10


my_list = [1, 2]
func1(my_list)
print(my_list)


# 只有 = 可以改变引用
# 可变参数做参数，在函数内部，如果不使用 = 直接修改形参的引用，对形参进行的数据修改会同步到实参中
# 对于列表来说， += 的本质是extend操作

def func2(list1):
    list1 += [1, 2]


my_list = ['a', 'b']
func2(my_list)
print(my_list)

