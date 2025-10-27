"""
TestLoader的使用
"""
import unittest

# 2.实例化加载对象并添加用例
# unittest.TestLoader().discover('用例所在的路劲', '用例的代码文件名')
suite = unittest.TestLoader().discover('./case', '*_test*.py')

"""
# 3.实例化运行对象
runner = unittest.TextTestRunner()

# 4.执行
runner.run(suite)
"""
# 可以将3 4 步变为一步
unittest.TextTestRunner().run(suite)
