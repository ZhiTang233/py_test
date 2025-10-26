"""
try:
    书写可能发生异常的代码
except：
    发生异常执行的代码

try:
    书写可能发生异常的代码
except 异常类型:
    #  只能捕获指定类型的异常
except 异常类型:
    发生异常执行的代码
"""

# 完整版
"""
try:
    发生异常的代码
except 异常类型1:
    发生异常类型1执行的代码
except Exception as 变量:
    # print(变量)打印异常信息
    发生其他类型的异常
else:
    没有发生异常会执行的代码
finally：
    不管有没有异常，都会执行

"""
try:
    num = input('输入数字')
    num = int(num)
    print(num)
    a = 10 / num
    print(f'a: {a}')
except Exception as e:
    print(f'错误信息为: {e}')
else:
    print('没有异常我会执行')
finally:
    print('不管有没有异常，我都会执行')
