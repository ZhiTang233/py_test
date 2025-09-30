name = '小明'
age = 18
height = 1.71
stu_num = 1
num = 90

print(f'我的名字是{name}，年龄是{age}，身高是{height}m，学号{stu_num}，本次考试的及格率{num}%')
print(f'我的名字是{name}，年龄是{age}，身高是{height}m，学号{stu_num: 06d}，本次考试的及格率{num}%')
print(f'我的名字是{name}，年龄是{age}，身高是{height}m，学号{stu_num: 06d}，\n本次考试的及格率{num}%')
print('我的名字是{}，年龄是{}，身高是{}m，学号{}，本次考试的及格率{}%'.format(name, age, height, stu_num, num))
print('我的名字是{}，年龄是{}，身高是{:.3f}m，学号{}，本次考试的及格率{}%'.format(name, age, height, stu_num, num))
