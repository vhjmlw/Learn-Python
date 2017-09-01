#-*- coding:utf-8 -*-

i = 1
while i <= 5:
    j = 1
    while j <= 5:
        if j == 5:
            print('*')
        else:
            print('*',end='')
        j += 1
    i += 1
