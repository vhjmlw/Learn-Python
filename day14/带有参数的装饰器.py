# -*- coding:utf-8 -*-

"带有参数的装饰器，就是在普通装饰器的外面在嵌套一层函数，本质还是闭包的进一步应用"

__author__ = '建磊'

def decorator(tmp):

    def fn(func):
        def wrapper(*args,**kw):
            print('装饰器的参数：%s'%tmp)
            return func(*args,**kw)
        return wrapper

    return fn

@decorator('hello world')
def demo():
    print('这里是demo函数')

demo()
