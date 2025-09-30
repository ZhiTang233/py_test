# 1. 获取你输入的字符串
result = input('请输入一个字符串：')
# 2. 遍历打印这个字符串
for i in result:
    if i == 'e':
        continue
    print(i)

print('-' * 30)
for i in result:
    if i != 'e':
        print(i)
