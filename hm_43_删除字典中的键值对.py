my_dict = {'name': '小明', 'age': 19, 'like': ['抽烟', '喝酒', '烫头', '学习'], 'sex': '男'}
# 删除 sex 键值对
del my_dict['sex']
print(my_dict)

# 字典.pop('键')
my_dict.pop('age')
print(my_dict)

# 删除抽烟的爱好
my_dict['like'].pop(0)
print(my_dict)

my_dict['like'].remove('喝酒')
print(my_dict)

# 清空键值对
my_dict.clear()
print(my_dict)
