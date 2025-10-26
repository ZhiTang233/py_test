with open('b.txt', encoding='utf-8') as f:  # 默认r
    buf = f.readline()
    print(buf)
    print(f.readline())

with open('b.txt', encoding='utf-8') as f:
    for i in f:
        print(i, end='\n')
# read和readline读到文末，返回一个空字符串
with open('b.txt', encoding='utf-8') as f:
    while True:
        buf = f.readline()
        if len(buf) == 0:
            break
        else:
            print(buf, end='\n')

# 在容器中，容器为空，即容器的数据的个数为0，表示false，其余都是True
with open('b.txt', encoding='utf-8') as f:
    while True:
        buf = f.readline()
        if buf:  # if len(buf) != 0
            print(buf)
        else:
            break
