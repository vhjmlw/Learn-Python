# coding:utf-8 -*-

"多个fork，每次fork都乘以2"

__author__ = '建磊'

import os

id = os.fork()
if id == 0:
    print('1')
else:
    print('2')

id = os.fork()
if id == 0:
    print('11')
else:
    print('22')
