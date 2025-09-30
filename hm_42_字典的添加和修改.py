# 定义字典
my_dict = {"name": "小明", "age": 18, "like": ['抽烟', '喝酒', '烫头']}
print(my_dict)

# 1. 添加性别信息sex
my_dict['sex'] = '男'
print(my_dict)

# 2. 修改年龄为19
my_dict['age'] = 19
print(my_dict)

# 3. 添加一个爱好
my_dict['like'].append('学习')
print(my_dict)
