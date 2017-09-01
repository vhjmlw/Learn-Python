# -*- coding:utf-8 -*-

'类装饰器'

__author__ = '建磊'

class Demo(object):

    def __init__(self,func):
        print('__init__')
        self.__func = func

    def __call__(self,*args,**kw):
        print('__call__')
        return self.__func(*args,**kw)

@Demo
def fn(tmp):
    print(tmp)

fn('hello world')
