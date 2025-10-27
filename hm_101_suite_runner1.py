"""
学习TestSuite TestRunner
1.导包
2.实例化（创建对象）套件对象
3.使用套件对象添加用例方法
4.实例化运行对象
5.使用运行对象去执行套件对象
"""
import unittest

from hm_100_testcase1 import TestDemo1
from hm_100_testcase2 import TestDemo2

suite = unittest.TestSuite()

# 方式二 将一个测试类中的所以方法进行添加
# 套件对象.addTest(unittest.makeSuite()测试类名) py3.x移除
# suite.addTest(unittest.makeSuite(TestDemo1))
# suite.addTest(unittest.makeSuite(TestDemo2))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDemo1))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDemo2))

runner = unittest.TextTestRunner()

runner.run(suite)
