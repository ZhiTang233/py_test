# 1. 类实例化的方法（不常用
# 1.1 定义空列表（没有任何数据的列表
# 变量 = list()
list1 = list()
print(type(list1), list)

# 1.2 类型转换 list容器 将其他的容器转换为列表
# 转换字符串会将字符串中的每个字符作为一个数据存入列表中
list2 = list('list')
print(type(list2), list2)

# 2. 直接使用[]进行定义（常用
# 2.1 定义空列表
my_list = []
print(my_list)
# 2.2 定义非空列表
my_list1 = [1, '小明', '3.14', False]
print(my_list1)
