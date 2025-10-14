"""
字典没有下标的概念 获取数据值用key键来获取

"""
my_dict = {'name': '小明', 'age': 19, 'like': ['抽烟', '喝酒', '烫头', '学习']}
# 1.获取名字
print(my_dict['name'])
print(my_dict.get('name'))

# 2. 获取sex性别
# print(my_dict['sex']) 代码报错,key不存在
print(my_dict.get('sex'))
print(my_dict.get('sex', '保密'))

# 3.获取第二个爱好
print(my_dict['like'][1])
print(my_dict.get('like')[1])
