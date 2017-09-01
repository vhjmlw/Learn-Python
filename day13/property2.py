# -*- coding:utf-8 -*-

'property的第二种用法'

__author__ = '建磊'


class Person(object):

    def __init__(self):
        super(object,self).__init__()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if name == 'jianlei':
            self.__name = name
        else:
            print('no no no')

jianlei = Person()
jianlei.name = 'vhjmlw'
jianlei.name = 'jianlei'
print(jianlei.name)
