# coding:utf-8 -*-

"Pool创建子进程同步"

__author__ = '建磊'

import os
import time
from multiprocessing import Pool

def fn(index):
    time.sleep(1)
    print('当前子进程索引：%s，ID：%s，父进程ID：%s'%(index,os.getpid(),os.getppid()))

def main():
    po = Pool(5)
    for x in range(20):
        po.apply(fn,args=(x,))
    po.close()
    po.join()
    print('父进程结束')

if __name__ == '__main__':
    main()
