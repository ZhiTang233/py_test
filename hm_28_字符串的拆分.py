str1 = 'hello world and itheima and Python'
# 1. 将str1按照and字符拆分
result1 = str1.split('and')
print(result1)

# 2. 将str1按照and字符拆分，拆分一次
result2 = str1.split('and', 1)
print(result2)

# 3. 按照空白字符进行切割
result3 = str1.split()
print(result3)

# 4. 按照空白字符进行切割，拆分一次
result4 = str1.split(maxsplit=1)
print(result4)
