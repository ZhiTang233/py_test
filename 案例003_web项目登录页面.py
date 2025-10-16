"""
某web项目登录页面包含；用户名，密码，验证码，登录按钮和登录方法
类名:loginPage
属性 用户名 username 密码 password 验证码 code 登录按钮 button
方法 登录(login)
"""


class LoginPage:
    def __init__(self, username, password, code):
        self.username = username
        self.password = password
        self.code = code
        self.button = '登录'

    def login(self):
        print(f'1.输入用户名: {self.username}')
        print(f'2.输入密码: {self.password}')
        print(f'3.输入验证码: {self.code}')
        print(f'4.点击按钮: {self.button}')


login = LoginPage('admin', '123456', '8888')
login.login()
