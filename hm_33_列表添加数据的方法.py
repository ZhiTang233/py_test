my_list = []
print(my_list)

# 1.想列表中添加数据
my_list.append('hhhh')
print(my_list)

# 2. 向列表的尾部添加
my_list.append('wowowo')
print(my_list)

# 3. 在下标位置为1的位置添加数据
my_list.insert(1, '厉害')
print(my_list)

# 4. 在下标位置为1的位置添加数据
my_list.insert(1, '你')
print(my_list)

# 5.定义新的列表list1
list1 = ['不是', '哥们']
print(list1)

# 将list1 作为一个整体添加到my_list

my_list.extend(list1)
print(my_list)
