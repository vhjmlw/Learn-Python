# -*- coding:utf-8 -*-

file_read = open('写文件.py','r')

file_write = open('复制后的文件.py','w')

for x in file_read.readlines():
    file_write.write(x)

file_read.close()
file_write.close()

