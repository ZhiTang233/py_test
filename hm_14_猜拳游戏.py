import random
# 自己出拳 石头(1) / 剪刀（2)/ 布（3）
player = int(input('请出拳石头(1) / 剪刀（2)/ 布（3）'))   # 不要忘了类型转换

computer = random.randint(1, 3)
if(player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print('恭喜你获得胜利')
elif player == computer:
    print('平局')
else:
    print('输了，不要放弃，再来一局')
