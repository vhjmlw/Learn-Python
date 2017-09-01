# -*- coding:utf-8 -*-

class Student():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我的名字叫：%s，我的年龄是：%d'%(self.name,self.age)

    def think(self):
        print('%s can think'%self.name)


jianlei = Student('建磊',18)
print(jianlei)
xunan = Student('旭楠',18)
print(xunan)
