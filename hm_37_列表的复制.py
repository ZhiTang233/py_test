my_list = [1, 2, 3]
my_list1 = my_list[:]
print('my_list:', my_list)
print('my_list1:', my_list1)

my_list1[1] = 22
print('my_list:', my_list)
print('my_list1:', my_list1)

print('-' * 30)

my_list2 = my_list.copy()
print('my_list:', my_list)
print('my_list2:', my_list2)

print('-' * 30)

my_list2[2] = 33
print('my_list', my_list)
print('my_list2', my_list2)
