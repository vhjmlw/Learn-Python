# -*- coding:utf-8 -*-

class Student(object):

    obj = None
    count_flag = 0

    def __init__(self,name,age):
        if Student.count_flag == 0:
            self.name = name
            self.age = age
            Student.count_flag = 1

    def __new__(cls,name,age):
        if cls.obj == None:
            cls.obj = object.__new__(cls)
            return cls.obj
        else:
            return cls.obj

jianlei = Student('建磊',18)
print(jianlei.name)
xunan = Student('旭楠',20)
print(xunan.name)
print(id(jianlei))
print(id(xunan))
