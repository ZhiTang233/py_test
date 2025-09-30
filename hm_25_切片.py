# 字符串[start:end:step]

# 切片会得到一个字符串，即可以获取字符串中的多个字符
str1 = 'abcdefg'
# 1. 获取abc字符
print(str1[0:3:1])
# 1.1如果步长是1可以不写，最后一个冒号也不写
print(str1[0:3])
# 1.2如果开始位置为0，可以不写， 但是冒号必须有
print(str1[:3])

# 2. 获取efg字符
print(str1[4:7])
print(str1[4:6])
print(str1[4:5])
print(str1[4:4])
print(str1[-3:7])
# 2.1 如果最后一个字符也要取，可以不写，但是冒号必须有
print(str1[4:])
# 2.2 如果开始和结束都不写，获取全部内容，但是冒号必有
print(str1[:])

# 3.获取 aceg
print(str1[0:7:2])
print(str1[0:7:2])

# 特殊应用 步长为负数
print(str1[::-1])
