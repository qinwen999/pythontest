# coding=utf-8
# -*- coding: UTF-8 -*- 
'''
Created on 2016/2/25

@author: Kevin
'''
print u'你好！'

def conditions():
    #str='kevin'
    
    i = 10;j=1
    str='road'
    n = int(raw_input("enter a number:"))

    if n == i:
        print "equal"
    elif n < i:
        print "lower"
    else:
        print "higher"

print 'dddddd'

def loop1():
    for i in range(0, 10,1):
        print i

def loop2():
    count=5
    while count>0:
        print count
        count=count-1
    else:
        print 'over'
        
def var():
    i=0
    mystr='hello python' 
    mystr2="hello"
    a = b = c = 1
    d, e, f = 1, 2, "john"
    
    #列表是可变的有序表复合数据类型
    mylist = [ 'abcd', 786 , 2.23, 'john', 70.2 ]

   
    #元组是类似于列表中的序列数据类型,但是tuple初始化就不能修改
    mytuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )

    
    
    #字典
    mydict = {'name': 'john','code':6734, 'dept': 'sales','a':'b'}
    
    print mystr[0]  #第一个元素
    print mystr * 2   #字符串内容*2

    mylist.append('test')
    print mylist
    print mylist[3:] #第一个元素到最后一个
    print mylist[-1]  # 最后一个元素
    mylist[2] = 1000
    print mylist[2]

    #遍历list
    for i in mylist:
        print i
    else:
        pass


    print mytuple[2:4] #第二个元素和第四个元素之间，不包括第四个元素
    #tuple[2] = 1000  #元组不能改变，元组内数值的大小
    print mytuple[2]

    print '************'
    print mydict
    print mydict['name']
    print mydict.values()
    

    


if __name__ == '__main__':
    #conditions()
    #loop1()
    #print r'test'
    #loop2()
    var()


