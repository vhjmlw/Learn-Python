# -*- coding:utf-8 -*-

"全局变量在多个进程中不共享"

__author__ = '建磊'

import os
import time

name = 'jianlei'
print('全局变量name的初始值：%s'%name)
id = os.fork()
if id == 0:
    print('---子---')
    name = 'vhjmlw'
    print('子：全局变量name的值：%s'%name)
else:
    print('---父---')
    time.sleep(5)
    print('父：全局变量name的值：%s'%name)
