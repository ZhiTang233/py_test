"""
json.dump(Python中的数据类型, 文件对象)
"""
import json

my_list = [('admin', '123456', '登录成功'), ('root', '123456', '登录失败'), ('admin', '123456', '登录失败')]

with open('info003.json', 'w', encoding='utf-8') as f:
    # json.dump(my_list, f)
    # json.dump(my_list, f, ensure_ascii=False)  # 直接显示中文
    json.dump(my_list, f, ensure_ascii=False, indent=2)  # 显示缩进
