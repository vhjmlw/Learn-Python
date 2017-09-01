# -*- coding:utf-8 -*-

"使用Process的子类创建子进程"

__author__ = '建磊'

import os
import time
from multiprocessing import Process

class SubProcess(Process):

    def __init__(self):
        super(Process,self).__init__()

    def run(self):
        print('子进程开始执行')
        print('子进程的ID：%s，父进程的ID：%s'%(os.getpid(),os.getppid()))
        print('子进程结束执行')

p = SubProcess()
p.start()
p.join()
print('主进程的ID：%s'%os.getpid())

