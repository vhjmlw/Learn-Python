# -*- coding:utf-8 -*-

"解析装饰器的原理，本质上是闭包的应用"

__author__ = '建磊'

def decorator(func):

    def wrapper():
        print('这里是对func函数功能的扩展')
        return  func()

    return wrapper

def demo1():
    print('demo1')

def demo2():
    print('demo2')

demo1 = decorator(demo1)

demo2 = decorator(demo2)

if __name__ == '__main__':
    demo1()
    demo2()
