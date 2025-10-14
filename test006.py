# 定义一个函数my_max，包含两个参数，函数的作用是将两个数据中比较大的数进行返回
def my_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


# 调用函数并打印结果
result = my_max(10, 20)
print(result)  # 输出 20
