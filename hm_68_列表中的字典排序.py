user_list = [
    {'name': 'zhang', 'age': 18},
    {'name': 'lili', 'age': 19},
    {'name': 'haha', 'age': 20}
]

# 列表的排序，默认是对列表的数据进行比大小，可以对数字类型和字符串进行比大小
# 字典需要sort中的key这个参数 来指定字典大小的方法
# key这个参数，需要传递一个函数，一般为匿名函数 字典的排序 需要根据字典的键进行排序
# 使用匿名函数返回字典的键对应的值
# 列表.sort(key=lambda x: x['键'])
user_list.sort(key=lambda x: x['age'])
user_list.sort(key=lambda x: x['age'], reverse=True)
print(user_list)


"""
匿名函数中的参数是列表中的数据 sort函数内部会调用key这个函数
从列表中的获取函数的返回值，对返回值进行比大小操作
"""

"""
字符串大小，是比较字符对应的ASCII码值
ord(字符)  # 获取字符对应的ASCII的值
chr(ASCII值)  # 获取对应的字符

'abc' < 'abb' F
"""