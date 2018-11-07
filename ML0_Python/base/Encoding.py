
# -*- coding: UTF-8 -*- 
'''
Created on 2017年4月10日

@author: Kevin
'''
import sys

aa=123;ab=123.6;ac="你好世界"
print aa
print ab
print ac


if __name__ == '__main__':
    print sys.getdefaultencoding()
    a='你好'
    b=u'你好'
    c="你好"
    
    print a+'\n'
    print b
    print len(a)
    print len(b)