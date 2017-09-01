# -*- coding:utf-8 -*-

"使用multiprocessing模块创建模块"

__author__ = '建磊'

import time
from multiprocessing import Process

def subProcess():
    while True:
        print('子进程')
        time.sleep(1)

p = Process(target=subProcess)

p.start()

while True:
    print('父进程')
    time.sleep(1)

