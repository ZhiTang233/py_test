import random
import json

my_list = []
for i in range(10):
    num = random.randint(1, 20)
    my_list.append(num)


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(my_list, f)


with open('data.json', encoding='utf-8') as f:
    data_list = json.load(f)
    data_list.sort(reverse=True)
    print(data_list)
    print(data_list[:5])
    