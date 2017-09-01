# -*- coding:utf-8 -*-

"多个装饰器同时装饰一个函数的时候，装饰器直接执行的顺序问题"

__author__ = '建磊'

def decorator1(func):
    print('decorator1')
    def wrapper1(*args,**kw):
        print('wrapper1')
        return func(*args,**kw)

    return wrapper1

def decorator2(func):
    print('decorator2')
    def wrapper2(*args,**kw):
        print('wrapper2')
        return func(*args,**kw)

    return wrapper2

@decorator2
@decorator1
def demo():
    print('demo')

# 打印顺序应该是：decorator1  decorator2  wrapper2  wrapper1  demo
demo()
