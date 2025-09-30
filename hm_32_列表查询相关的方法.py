my_list = [1, 3, 5, 7, 2, 3]
# 找数据3出现的下标
num = my_list.index(3)
print(num)

# 找数据4出现的下标
if 4 in my_list:
    num1 = my_list.index(4)
    print(num1)
else:
    print('不存在')

# my_list.count(4)统计
if my_list.count(4) > 0:
    num1 = my_list.index(4)
    print(num1)
else:
    print('不存在')
