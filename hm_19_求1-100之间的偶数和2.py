num = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        num += i
    # 改变计数器
    i += 1
print('偶数和：', num)
