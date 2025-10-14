def my_sum(a, b):
    num = a + b
    # print(num)
    # 想要在后续的代码中使用，需要使用return将求和的结果返回
    return num


# 1.函数中没有print 只有return 想要查看结果 需要在调用的时候用print
print(my_sum(1, 2))
# 2.想要在后续代码使用，需要保存数据，需要使用变量来接收函数返回值
result = my_sum(10, 20)
print('直接使用', result)
print('进行计算', result + 10)
