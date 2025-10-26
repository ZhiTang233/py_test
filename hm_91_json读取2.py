import json

with open('info001.json', encoding='utf-8') as f:
    info_list = json.load(f)
    for info in info_list:
        print(info.get('name'), info.get('age'), info.get('address').get('city'))
