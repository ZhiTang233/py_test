my_dict = {'登录': [{'desc': '正确的用户名密码', 'username': 'admin', 'password': '123456', 'expect': '登录成功'},
                  {'desc': '错误的用户名', 'username': 'root', 'password': '123456', 'expect': '登录失败'},
                  {'desc': '错误的密码', 'username': 'admin', 'password': '123456', 'expect': '登录失败'},
                  {'desc': '错误的用户名和密码', 'username': 'aaaa', 'password': '123123', 'expect': '登录失败'}
                  ],
           '注册': [{'desc': '注册1', 'username': 'abcd', 'password': '123456'},
                  {'desc': '注册1', 'username': 'xyz', 'password': '123456'}]}
"""
1.自定义程序 实现如下要求
2.能够获取测试人员输入的信息（登录/测试
3.获取每组测试数据的用户名，密码和预期结果 组成一下的数据格式进行打印
"""
opt = input('请输入要获取的数据')
info_list = []
if opt == '登录':
    print('获取登录数据')
    for d in my_dict.get('登录'):
        my_tuple = (d.get('username'), d.get('password', d.get('expect')))
        info_list.append(my_tuple)
    print(info_list)
elif opt == '注册':
    print('获取注册数据')
    for d in my_dict.get('注册'):
        my_tuple = (d.get('username'), d.get('password'), d.get('expect'))
        info_list.append(my_tuple)
    print(info_list)
else:
    print('输入错误')
print(info_list)
