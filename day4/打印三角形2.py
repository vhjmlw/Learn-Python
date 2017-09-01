# -*- coding:utf-8 -*-

row = int(input('想要打印多少行的。。。'))
i = 1
while i <= row:
    j = 1
    while j <= i:
        if j == i:
            print('*')
        else:
            print('*',end='')
        j += 1
    i += 1
