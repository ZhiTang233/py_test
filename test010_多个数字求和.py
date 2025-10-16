# 定义函数my_sum，可以对任意多个数字进行求和
def my_sum(*args):  # args是元组类型
    num = 0
    for i in args:
        num += i
    print(num)


my_sum(1, 2)
my_sum(2, 1.2)


def my_sum1(*args):
    num = sum(args)
    return num


result = my_sum1(1, 2, 3)
print(result)


def my_sum2(*args, **kwargs):
    num = 0
    for i in args:
        num += i

    for j in kwargs:
        num += j

    print(num)


my_sum2(1, 2, a=3, b=4)
