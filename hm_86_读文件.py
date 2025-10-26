f = open('a.txt', 'r', encoding='utf-8')
buf = f.read()
print(buf)
f.close()

# r 方式打开文件，如果文件不存在，代码报错
