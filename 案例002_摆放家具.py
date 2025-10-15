"""
1.房子house有户型 总面积 和 家具名称列表
    新房子没有任何的家具
2.家具house item 有名字 和 占地面积
    床bed占地4平米
    衣柜chest占地2平米
    餐桌table占地1.5平米
3.将以上三件家具 添加 到 房子中
4.打印房子时要求输出：户型、总面积、剩余面具、家具名称列表

剩余面具
1.在创建房子对象时，定义一个剩余面积的属性，初始值和总面积相等
2.当调用add_item方法 向房间添加家具时，让剩余面积 -= 家具面积

类名：房子类 House
属性：户型 name 总面积 total_area 家具名称列表item_list = []
    剩余面积：free_area
方法：__init__,__str__
添加家具方法 add_item()
    判断房子的剩余面积和总面积关系
    修改房子的剩余面积
    修改房子的家具名称列表

类名：家具类 HouseItem
属性：名字 name 占地面积 area
方法：__init__ __str__
"""


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'{self.name}, 占地{self.area}平米'


class House:
    def __init__(self, house_type, total_area):
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area
        self.item_list = []

    def add_item(self, item):
        if item.area > self.free_area:
            print(f'无法添加{item.name}, 剩余面积不足')
            return False

        self.item_list.append(item.name)
        self.free_area -= item.area
        print(f'添加成功{item.name}')
        return True

    def __str__(self):
        return (f'户型: {self.house_type}\n'
                f'总面积: {self.total_area: .1f}平分\n'
                f'剩余面积: {self.free_area: .1f}平分\n'
                f'家具列表: {self.item_list}')


bed = HouseItem('床', 4)

print('创建的家具:')
print(bed)

print('-' * 30)

my_house = House('三室一厅', 120)
print('创建的房子:')
print(my_house)

print('-' * 30)

print('添加家具:')
my_house.add_item(bed)

print('-' * 30)

print('最终房子信息:')
print(my_house)
