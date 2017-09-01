# -*- coding:utf-8 -*-

def demo1():
    print('demo1')

def demo2():
    print('demo2')

name = 'jianlei'

class Student(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print('%s can speak'%self.name)

__all__ = ['demo1','Student']
