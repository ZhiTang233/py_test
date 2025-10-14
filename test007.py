# 定义一个函数my_sum接收一个参数n，在函数中计算1+2+3+...+n的值，并在函数中打印求和结果
def my_sum(n):
    i = 0
    num = 0
    while i <= n:
        num += i
        i += 1
    print('求和的结果为', num)


my_sum(100)
