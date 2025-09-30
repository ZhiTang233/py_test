# 定义变量 姓名年龄 身高
name = '小明'
age = 18
height = 1.71

# 要求按照以下个数输出个人信息
# 我的名字是xx，年龄是xx，身高是xx m
print('我的年龄是%s,年龄是 %d,身高是%.2fm' % (name, age, height))
# 小数默认显示6位，%.nf

# 补充
stu_num = 1
# 我的学号是000001
print('我的学号是%d' % stu_num)
# %0nd
print('我的学号是%06d' % stu_num)
print('我的学号是%6d' % stu_num)


num = 90
# 格式化中显示% 需要用到两个%%
print('某次考试的及格率为 %d%%' % num)

# 撤销 ctrl z
# 删除一行 Ctrl x
# 复制粘贴一行 Ctrl d
# 快速在代码下方 新建一行 shift 回车
