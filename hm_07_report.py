import unittest
from htmltestreport import HTMLTestReport

from hm_05_pa import TestLogin

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLogin))

runner = HTMLTestReport('test_add_report.html', '加法用例测试报告', 'xxx')
runner.run(suite)
