"""
代码的目的：学习TestCase模块的书写
1.导包
2.自定义测试类
3.书写测试方法
4.执行测试
4.1将光标放在 类名的后边 运行，会执行类中的所以测试方法
4.2将光标放在 方法名的后边 运行，只执行test_开头
"""

import unittest


class TestDemo1(unittest.TestCase):
    #  目前没有 用print代替
    def test_method1(self):
        print('测试方法1-1')

    def test_method2(self):
        print('测试方法1-2')


