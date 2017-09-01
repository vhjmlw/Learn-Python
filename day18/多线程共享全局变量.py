# -*- coding:utf-8 -*-

"多个线程之间共享全局变量"

__author__ = '建磊'

import threading
import time

num = 100
print('执行线程前，全局变量num的值为：%s'%num)

def main():
    def fn1():
        global num
        for x in range(10):
            num += 1

    def fn2():
        global num
        print('线程执行后，全局变量num的值为：%s'%num)

    th1 = threading.Thread(target=fn1)
    th1.start()
    time.sleep(1)
    th2 = threading.Thread(target=fn2)
    th2.start()
    print('所有的线程执行后，全局变量num的值为：%s'%num)

if __name__ == '__main__':
    main()
