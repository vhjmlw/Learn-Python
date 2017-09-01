# -*- coding:utf-8 -*-

"使用Queue实现进程间通讯，Pool创建子进程"

__author__ = '建磊'

import os
from multiprocessing import Manager,Pool

def read(queue):
    for x in 'hello':
        queue.put(x)

def write(queue):
    while True:
        if not queue.empty():
            print(queue.get())
        else:
            break

def main():
    queue = Manager().Queue()
    po = Pool(5)
    po.apply(read,args=(queue,))
    po.apply(write,args=(queue,))
    po.close()
    po.join()

if __name__ == '__main__':
    main()
