import unittest

from tools001 import add


class TestAdd(unittest.TestCase):
    def test_method1(self):
        if add(1, 2) == 3:
            print('测试通过')
        else:
            print('测试不通过')

    def test_method2(self):
        if add(10, 20) == 30:
            print('测试通过')
        else:
            print('测试不通过')

    def test_method3(self):
        if add(2, 3) == 5:
            print('测试通过')
        else:
            print('测试不通过')
