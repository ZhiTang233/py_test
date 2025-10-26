import json


def read_data():
    new_list = []
    with open('info002.json', encoding='utf-8') as f:
        data = json.load(f)
        # print(data)
        for i in data:
            # print(i.get('username'), i.get('password'), i.get('expect'))
            new_list.append((i.get('username'), i.get('password'), i.get('expect')))

        # print(new_list)
    return new_list


result = read_data()
print(result)
