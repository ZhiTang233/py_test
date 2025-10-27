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

# 方式一 套件对象.addTest（测试类名（'方法名'）） #建议复制
suite.addTest(TestDemo1('test_method1'))
suite.addTest(TestDemo1('test_method2'))
suite.addTest(TestDemo2('test_method1'))
suite.addTest(TestDemo2('test_method2'))

runner = unittest.TextTestRunner()

runner.run(suite)
