# -*- coding:utf-8 -*-

"使用generator生成器实现裴波那切数列"

__author__ = '建磊'

def fib(n):
    a,b = 0,1
    m = 0
    while m < n:
        print(b)
        a,b = b,a+b
        m += 1

fib(10)
