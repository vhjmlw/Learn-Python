# -*- coding:utf-8 -*-

'使用Pool创建子进程'

__author__ = '建磊'

from multiprocessing import Pool
import os
import time

def func(index):
    """func方法不能声明在main方法里面
    否则会无法调用，？？？"""
    time.sleep(1)
    print('当前子进程的序号为：%s，ID为：%s，父进程ID为：%s'%(index,os.getpid(),os.getppid()))

def main():
    p = Pool(5)
    for x in range(10):
        p.apply_async(func,args=(x,))
    p.close()
    p.join()
    print('主进程结束')

if __name__ == '__main__':
    main()
