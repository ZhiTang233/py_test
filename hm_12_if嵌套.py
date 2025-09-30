# 取款机取钱的过程，假定 你的密码是123456，账户余额为1000
pwd = '123456'
money = 1000
# 1. 提示用户输入密码
password = input('请输入密码：')
# 2. 判断密码是否正确
if password == pwd:
    print('密码正确，登录成功')
    # 3. 密码正确后，提示输入取款的金额
    get_money = int(input('请输入要取款的金额：'))
    # 4. 判断取款的金额和余额的关系
    if money >= get_money:
        print('取款成功')
    else:
        print('余额不足')
else:
    print('密码有误，请再次尝试')

