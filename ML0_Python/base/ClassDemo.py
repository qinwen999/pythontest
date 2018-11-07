var=123456
class MyClass(object):
    '''
    classdocs

    '''
    i=123
    __a=456


    def __init__(self):
        '''
        Constructor
        '''
    def printvar(self):
        return self.i
    
    def printvar2(self,strb):
        return strb
    
    def __my(self): 
        return 0
    
    def __del__(self):
        print self.i
    
def mytest():
    print 'test'

def mytest2(mytest):
    print 'test'


class MyClass2():
    '''
    classdocs

    '''
    i=123

    __j=321
    __a = 456


    def __init__(self):
        '''
        Constructor
        '''
    def printvar2(self):
        return self.i

    def printvar3(self):
        print self.__a
        return self.__a


if __name__ == '__main__':
    c2=MyClass2()
    print c2.printvar2()
    print c2.printvar3()

    print "*******"
    print c2.__a