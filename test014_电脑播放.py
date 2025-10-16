"""
类 电脑 Computer
属性 品牌 brand 价格 price
方法 播放 play_movie
"""


class Computer:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def play_movie(self, movie):
        print(f'{self.brand} 播放 {movie}')


xm = Computer('小米电脑', 4999)
mac = Computer('Mac', 14999)
xm.play_movie('葫芦娃')
mac.play_movie('猫和老鼠')
