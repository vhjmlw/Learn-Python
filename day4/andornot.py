#-*- coding:utf-8 -*-

self = input('你去吗？')
wife = input('你媳妇去吗？')

if self == '去' or wife == '去':
    print('这是能办成')
else:
    print('这事办不了')

if self =='去' and wife == '去':
    print('这事能办成')
else:
    print('这事办不了')

