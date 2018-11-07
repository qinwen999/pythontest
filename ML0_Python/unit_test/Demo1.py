import random
import unittest
import HTMLTestRunner

class TestDemo(unittest.TestCase):

    def setUp(self):
        pass

    def test_case1(self):
        self.assertEqual(1, 1)

    def test_case2(self):
        self.assertEqual(1, 2)

suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
unittest.TextTestRunner(verbosity=2).run(suite)

outfile = open("D:\Report2.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report',
                description='This demonstrates the report output by Prasanna.Yelsangikar.'
                )

runner.run(suite)