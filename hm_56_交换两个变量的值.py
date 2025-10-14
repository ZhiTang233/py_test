# 方法一：常规方法 引用第三个变量
a = 10
b = 20

c = a
a = b
b = c
print(a, b)

# 方法二：不适用第三个变量，使用数学中的方法
x = 10
y = 20
x = x + y
y = x - y
x = x - y
print(x, y)

# 方法三，重点掌握
a, b = b, a
print(a, b)

# 组包
c = a, b
print(type(c), c)

# 拆包
a, b = c
print(a, b)

x, y, z = [1, 2, 3]
print(x, y, z)
