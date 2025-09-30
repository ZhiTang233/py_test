
"""
元组的数据内容不能改变，列表中的可以改变
元祖使用() 列表使用[]
应用:在函数的传参或者返回值中使用，保证数据不会被改变
"""
# 类的实例化方式
# 1.1 定义空元组(不会使用
my_tuple1 = tuple()
print(type(my_tuple1), my_tuple1)

# 1.2 类型转换
# 可以将列表转换为元组 只需要将[]变为() 反之亦然
my_tuple2 = tuple([1, 2, 3])
print(my_tuple2)

# 转换字符串 和列表一样，只需要将列表[]变为()
my_tuple3 = tuple('hello')
print(my_tuple3)

# 2. 直接使用()定义
my_tuple4 = (1, '小王', 3.14, False)
print(my_tuple4)

# 特殊点 定义只有一个数据的元组时，数据后面必须有一个逗号
my_tuple5 = (1,)
print(my_tuple5)
print(my_tuple4[1])
