"""
不用自己去书写关闭文件的代码 自动关闭
"""

with open('a.txt', 'a', encoding='utf-8') as f:
    f.write('good good')
