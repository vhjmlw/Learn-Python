# -*- coding:utf-8 -*-

file = open('写文件.py','r')

for x in file.readlines():
    print(x)

file.close()
