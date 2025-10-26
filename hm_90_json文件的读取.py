"""
1.导包import json
2.读打开文件
3.读文件
json.load(文件对象)

返回的是字典(文件是对象)或者列表(文件中是数组)

"""

import json
with open('info.json', encoding='utf-8') as f:
    result = json.load(f)
    print(type(result))

    print(result.get('name'))
    print(result.get('address').get('city'))
