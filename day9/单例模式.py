# -*- coding:utf-8 -*-

class Student(object):

    obj = None

    def __init__(self,name):
        self.name = name

    def __new__(cls,name):
        if cls.obj == None:
            cls.obj = object.__new__(cls)
            return cls.obj
        else:
            return cls.obj

jianlei = Student('建磊')
print(jianlei.name)
xunan = Student('旭楠')
print(xunan.name)
print(id(jianlei))
print(id(xunan))
