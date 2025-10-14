# 定义一个函数login，函数接受两个参数，用户名username密码password
def login(username, password):
    if username == 'admin' and password == '123456':
        print('正确')
    else:
        print('错误')


user = input('用户名')
word = input('密码')
login(user, word)
