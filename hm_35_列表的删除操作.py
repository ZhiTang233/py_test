my_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# 1. 删除最后一个位置的数据
num = my_list.pop()
print('删除的数据为：', num)
print(my_list)

# 2. 删除下标为1的数据3
my_list.pop(1)
print(my_list)

# 3. 删除数据为7 的数据 如果没有就报错
my_list.remove(7)
print(my_list)

# 清空
my_list.clear()
print(my_list)
