"""
定义一个游戏类，包含实例属性 玩家名字 name
记录游戏最高分 top_score
方法show_help 输出游戏信息
    show_top_score 打印最高分
    start_game 开始游戏

使用随机数获取分数(10-100)
判断本次得分和最高分关系
输出本次得分
"""
import random


class Game:
    top_score = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_help():
        print('游戏规则')

    @classmethod
    def show_top_score(cls):
        print(f'游戏最高分: {Game.top_score}')

    def start_game(self):
        print(f'{self.name} 开始一局游戏', end='')
        score = random.randint(10, 100)
        print(f'本次得分{score}')
        if score > Game.top_score:
            Game.top_score = score


xw = Game('小王')
xw.start_game()
xw.show_top_score()
