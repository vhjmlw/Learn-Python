# -*- coding:utf-8 -*-

"同时使用property的两种方法"

__author__ = '建磊'

class Person(object):

    def __init__(self):
        super(object,self).__init__()

    def setName(self,name):
        if isinstance(name,str) and name == 'jianlei':
            self.__name = name
        else:
            print('no no no')

    def getName(self):
        return self.__name

    name = property(getName,setName)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if isinstance(age,int):
            self.__age = age
        else:
            print('oh no')

jianlei = Person()
jianlei.name = 'vhjmlw'
jianlei.name = 'jianlei'
print(jianlei.name)
jianlei.age = '18'
jianlei.age = 18
print(jianlei.age)
