# -*- coding: utf-8 -*-

class Animal:

    def run(self):
        print 'Animal is running..'

class Dog(Animal):

    def run(self):
        print 'Dog is running...'

class Cat(Animal):

    def run(self):
        print 'Cat is running...'

class CheckType:
    def check(self,animal):
        animal.run()

class Person:
    grade = 1

    def __init__(self, name):
        self.name = name

    def sayHi(self):  # 加self区别于普通函数
        print 'Hello, your name is?', self.name

    @staticmethod  # 声明静态，去掉则编译报错;还有静态方法不能访问类变量和实例变量
    def sayName():  # 使用了静态方法，则不能再使用self
        print "my name is king"  # ,grade,#self.name

    @classmethod  # 类方法
    def classMethod(cls):
        print("class method")



if __name__ == "__main__":

   c = CheckType()
   p1 = Dog()
   p12= Dog()
   p2 = Cat()
   p22 = Cat()
   print p1
   print p12

   c.check(p1)
   c.check(p2)

   p = Person("king")
   p.sayHi()
   p.sayName()
   p.classMethod()
   Person.classMethod()
   Person.sayName()






