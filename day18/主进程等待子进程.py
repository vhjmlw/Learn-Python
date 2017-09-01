# -*- coding:utf-8 -*-

"主进程等待所有的子进程结束后才结束"

__autor__ = '建磊'

import threading
import time

def main():

    def fn1():
        time.sleep(1)
        print('fn1')

    def fn2():
        time.sleep(1)
        print('fn2')

    th1 = threading.Thread(target=fn1)
    th2 = threading.Thread(target=fn2)
    th1.start()
    th2.start()

    print('主进程执行完毕，等待子进程。。。')

if __name__ == '__main__':
    main()
