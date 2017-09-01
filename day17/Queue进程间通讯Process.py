# -*- coding:utf-8 -*-

"使用Queue实现进程间通讯Process创建子进程"

__author__ = '建磊'

from multiprocessing import Process,Queue


def read(queue):
    for x in ['a','b','c','d']:
        queue.put(x)


def write(queue):
   # for x in range(queue.qsize()):  #为啥queue.qsize()报错？？？
       # tmp = queue.get()
       # print(tmp)
    while True:
        if not queue.empty():
            print(queue.get())
        else:
            break


def main():
    queue = Queue()
    p1 = Process(target=read,args=(queue,))
    p1.start()
    p1.join()
    p2 = Process(target=write,args=(queue,))
    p2.start()
    p2.join()
    print('主进程结束')

if __name__ == '__main__':
    main()
