"""
字典的数据有键key值value 组成 键表示数据的名字 值表示具体的数据
一个字典的键是唯一的 不能重复
"""
# 1.使用类实例化方法
my_dict = dict()
print(type(my_dict), my_dict)

# dict()不能直接转换为列表和元组,字符串

# 2. 直接使用{}定义
# 2.1 空字典
my_dict1 = {}
print(type(my_dict1), my_dict1)

# 2.2 非空字典
my_dict2 = {"name": "小明", "age": 18, "height": "1.70", "is_man": True, "like": ["抽烟", "喝酒", "烫头"]}
print(my_dict2)
print(len(my_dict2))
