class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 下方代码只是为了验证方法被调用
        # print('我是__init__')

    # 输出属性信息
    def show_info(self):
        print(f'小猫的名字是: {self.name}, 年龄是: {self.age}')


blue_cat = Cat('蓝猫', 2)
blue = blue_cat
blue.show_info()

block_cat = Cat('黑猫', 2)
block = block_cat
block.show_info()
