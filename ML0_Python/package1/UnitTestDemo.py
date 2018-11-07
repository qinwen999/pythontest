import unittest
class Test(unittest.TestCase):


    def setUp(self):
        print 'setup'
        pass


    def tearDown(self):
        print 'teardown'
        pass


    def testName1(self):
        self.assertEqual('hi', 'hi', 'test')
        print 'testName1'

    
    def testName2(self):
        self.assertEqual('hi', 'hi', 'test')
        print 'testName2'


    def Name3(self):
        self.assertEqual('hi', 'hi', 'test')
        print 'testName3'



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

    '''
    
    
    '''