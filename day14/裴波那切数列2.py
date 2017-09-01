# -*- coding:utf-8 -*-

'使用生成器实现裴波那切数列'

__author__ = '建磊'

def fib(n):
    m = 0
    a,b = 0,1
    while m < n:
        yield b
        a,b = b,a+b
        m +=1

generator = fib(5)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

