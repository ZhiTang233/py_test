import unittest

from hm_102_test import TestAdd

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAdd))
runner = unittest.TextTestRunner()
runner.run(suite)
