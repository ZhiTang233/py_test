# 定义函数my_sum,求1-100的偶数和
def my_sum():
    num1 = 0
    for i in range(1, 101):
        if i % 2 == 0:
            num1 += i
    print(num1)


my_sum()
