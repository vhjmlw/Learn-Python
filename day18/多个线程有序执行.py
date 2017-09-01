# -*- coding:utf-8 -*-

'多个线程有序执行'

__author__ = '建磊'

from threading import Thread
from threading import Lock
import time

def fn1():
    while True:
        if lock1.acquire():
            print('fn1上锁成功')
            time.sleep(1)
            lock2.release()

def fn2():
    while True:
        if lock2.acquire():
            print('fn2上锁成功')
            time.sleep(1)
            lock3.release()

def fn3():
    while True:
        if lock3.acquire():
            print('fn3上锁成功')
            time.sleep(1)
            lock1.release()

lock1 = Lock()
lock2 = Lock()
lock3 = Lock()
#下面两行的代码的位置很重要，
#要放在start的前面，不能放在最后面
lock2.acquire()
lock3.acquire()

th1 = Thread(target=fn1)
th1.start()
th2 = Thread(target=fn2)
th2.start()
th3 = Thread(target=fn3)
th3.start()

