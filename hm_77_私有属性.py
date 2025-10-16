class Person:
    def __init__(self, name, age):
        self.name = name
        # 私有的本质，是python解释器执行代码，发现属性名或者方法名前有__,会将这个名字重命名
        # 会在这个名字的前边加上_类名前缀，即self.__age -> self._Person__age
        self.__age = age  # 定义私有属性，属性名前加两个_

    def __str__(self):  # 在类内部可以直接访问私有属性
        return f'名字: {self.name}, 年龄: {self.__age}'


xm = Person('小明', 18)
print(xm)
print(xm.__dict__)
# print(xm.__age) 报错，在类外部不能直接使用私有属性
xm.__age = 20  # 这个不是修改私有属性，是添加一个公有的属性__age
print(xm)
print(xm.__dict__)

print(xm._Person__age)  # 能修改但是不建议
xm._Person__age = 19
print(xm)

# 补充:
# 对象.__dict__ 魔法属性，可以将对象具有的属性组成字典返回
