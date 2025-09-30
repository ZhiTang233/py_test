import random
name_list = []
for i in range(5):
    name = input('请输入5个名字')
    name_list.append(name)

num = random.randint(0, 4)
print(name_list[num])
