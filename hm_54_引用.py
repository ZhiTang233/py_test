a = 1  # 将数据1 的引用存到a对应的内存中
print('a', id(a))

b = a  # 将变量a 中的引用 保存到变量 b
print('b', id(b))

a = 10  # 将数据10的地址保存到a对应的地址
print('a', id(a))

print('b', id(b))
