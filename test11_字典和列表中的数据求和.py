# 将字典和列表中的数据使用my_sum函数进行求和
my_list = [1, 2, 3, 4]
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def my_sum2(*args, **kwargs):
    num = 0
    for i in args:
        num += i

    for j in kwargs.values():
        num += j

    print(num)


# 想要将列表中的数据 分别作为位置参数 进行传参 需要对列表进行拆包操作
my_sum2(*my_list)
# 想要将字典中的数据，作为关键字传参，需要使用**对字典进行拆包
my_sum2(**my_dict)
