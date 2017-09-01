# -*- coding:utf-8 -*-

'property的第一种用法'

__author__ = '建磊'

class Person(object):

    def __init__(self):
        super(object,self).__init__()

    def setName(self,name):
        if isinstance(name,str):
            self.__name = name
        else:
            print('name应该是字符串类型')

    def getName(self):
        return self.__name

    name = property(getName,setName)

jianlei = Person()

jianlei.name = 18
jianlei.name = 'jianlei'
print(jianlei.name)
