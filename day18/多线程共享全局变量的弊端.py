# -*- coding:utf-8 -*-

"多个线程共享全局变量的弊端"

__author__ = '建磊'

import time
import threading

num = 0

def main():
    def fn1():
        global num
        for x in range(1000000):
            num += 1

    def fn2():
        global num
        for x in range(1000000):
            num += 1

    th1 = threading.Thread(target=fn1)
    th1.start()
    #time.sleep(3)
    th2 = threading.Thread(target=fn2)
    th2.start()
    time.sleep(3)
    print('全局变量num的值为：%s'%num)

if __name__ == '__main__':
    main()
