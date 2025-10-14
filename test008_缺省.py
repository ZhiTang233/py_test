# 函数接受两个参数 不传递性别信息 ，值为保密
def func(name, sex='保密'):
    print(f'姓名: {name}, 性别: {sex}')


func('x', 'x')
func('x')
