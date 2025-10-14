"""
函数中想要返回一个数据值，使用return 关键字
将多个数据值组成容器进行返回，一般是元组
"""


def calc(a, b):
    num = a + b
    num1 = a - b
    return num, num1


# 写法一
result = calc(1, 2)
print(result, result[0], result[1])

# 写法二，直接拆包
x, y = calc(10, 20)
print(x, y)
