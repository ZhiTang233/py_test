class Dog:
    count = 0

    def __init__(self, name):
        self.name = name  # 实例属性
        Dog.count += 1


print(Dog.count)
dog1 = Dog('校花')
print(Dog.count)
dog2 = Dog  # 不是创建对象 个数不变
dog3 = dog1  # 不是创建对象 个数不变
print(Dog.count)

dog4 = Dog('大黄')
print(Dog.count)

print('-' * 30)
# 可以使用 实例对象.类属性名 来获取类属性的值
print(dog1.count)
print(dog4.count)


