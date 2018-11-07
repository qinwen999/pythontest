# coding=utf-8

def read():
    myfile = open('hello.txt')
    try:
        all_the_text = myfile.read( )
        print '文件内容：'+all_the_text
    finally:
        myfile.close( )



def write():    
    context="test"
    f=open("hello.txt",'a')
    f.write(context);
    f.close()  
    

if __name__ == '__main__':
    write()
    read()