# -*- coding:utf-8 -*-

"Iterable和Iterator的区别"

__author__ = '建磊'

from collections import Iterable,Iterator

print(isinstance('123',Iterable))

print(isinstance([1,2,3],Iterable))

print(isinstance((1,2,3),Iterable))

print(isinstance({'name':'jianlei'},Iterable))

print(isinstance({1,2,3},Iterable))

print(isinstance((x for x in range(11)),Iterator))

print(isinstance('123',Iterator))

print(isinstance(iter('123'),Iterator))
