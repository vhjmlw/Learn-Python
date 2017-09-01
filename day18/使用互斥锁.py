# -*- coding:utf-8 -*-

'使用互斥锁避免多个线程同时更改同一个全局变量'

__author__ = '建磊'

from threading import Lock
from threading import Thread

num = 0

def main():

    def fn1():
        global num
        for x in range(1000000):
            lock.acquire()
            num += 1
            lock.release()
        print('fn1中的num：%s'%num)

    def fn2():
        global num
        for x in range(1000000):
            lock.acquire()
            num += 1
            lock.release()
        print('fn2中的num：%s'%num)

    lock = Lock()
    th1 = Thread(target=fn1)
    th1.start()
    th2 = Thread(target=fn2)
    th2.start()
    print('最终num的值为：%s'%num)

if __name__ == '__main__':
    main()
