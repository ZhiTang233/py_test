# 定义列表
my_list = ['hello', 'python', 'it', 'hello']

# 添加数据
my_list.append('heima')

# 删除第一个数据
my_list.pop(0)

# 删除it
my_list.remove('it')

# 修改
my_list[0] = 'wyg'

# 查
num = my_list.index('wyg')
print(num)
print(my_list[2])

# 统计
num1 = my_list.count('hello')
num2 = len(my_list)
print(num1)
print(num2)
