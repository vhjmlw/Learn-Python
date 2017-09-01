# -*- coding:utf-8 -*-

"getpid和getppid的用法"

__author__ = '建磊'

import os

id = os.fork()
if id == 0:
    print('当前子进程，ID为：%s，父进程ID为：%s'%(os.getpid(),os.getppid()))
else:
    print('当前父进程，ID为：%s，新创建的子进程的ID为：%s'%(os.getpid(),id))
