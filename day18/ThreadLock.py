# -*- coding:utf-8 -*-

'ThreadLocal'

__author__ = '建磊'

import time
from threading import local
from threading import Thread
import threading

thread_local = local()

def main():

    def fn():
        thread_local.name = threading.current_thread().name
        func()

    def func():
        name = thread_local.name
        print(name)

    th1 = Thread(target=fn)
    th2 = Thread(target=fn)
    th1.start()
    th2.start()

if __name__ == '__main__':
    main()
