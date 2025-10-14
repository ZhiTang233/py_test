"""
方式1.
遍历原列表中的数据判断在新列表是否存在，如果存在不管，如果不存在放在新列表中
遍历 for
判断是否存在 in
存入数据 append

方式2
在py中还有一种数据类型（容器 称为集合set
特点：集合中不能有重复的数据（如果有重复的数据会自动去重
可以使用集合的特点对列表去重
1.使用set（）类型转换将列表转换为集合类型
2.使用list（）类型转换将集合转换为列表
缺点：不能保证数据在原列表的顺序
"""
my_list = [3, 2, 1, 1, 2, 3, 1, 2, 3]

# new_list = list(set(my_list))
# print(new_list)

new_list = []
# for i in my_list:
#     if i in new_list:
#         pass
#     else:
#         new_list.append(i)
for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)
