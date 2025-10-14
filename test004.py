my_list = [{'id': 1, 'money': 20}, {'id': 2, 'money': 20}, {'id': 3, 'money': 30}, {'id': 4, 'money': 40}]
for i in my_list:
    if i.get('id') % 2 == 1:
        i['money'] = i.get('money') + 20
    else:
        i['money'] = i.get('money') + 10
print(my_list)
