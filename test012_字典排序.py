my_list = [{'name': 'd', 'age': 19},
           {'name': 'b', 'age': 16},
           {'name': 'a', 'age': 16},
           {'name': 'c', 'age': 20}]

my_list.sort(key=lambda x: x['age'], reverse=True)
print(my_list)
