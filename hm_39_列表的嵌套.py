person_info = ['张三', '18', '功能测试'], ['李四', '20', '自动化测试']
print(len(person_info))
print(person_info[0])
print(person_info[0][0])
print(person_info[0][0][0])

person_info[0][1] = '19'
print(person_info)

# 添加一个性别信息
person_info[1].append('男')
print(person_info)

# 将年龄信息删除
person_info[0].pop(1)
print(person_info)

person_info[1].remove('20')
print(person_info)
