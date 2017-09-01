# -*- coding:utf-8 -*-

'规避多线程共享全局变量的弊端'

__author__ = '建磊'

from threading import Thread

num = 0
flag = 0

def main():

    def fn1():
        global num
        global flag
        if flag == 0:
            for x in range(1000000):
                num += 1
            flag = 1
        print('fn1的num为：%s'%num)

    def fn2():
        global num
        global flag
        while True:
            if flag == 1:
                for x in range(1000000):
                    num += 1
                break
        print('fn2的num为：%s'%num)

    th1 = Thread(target=fn1)
    th1.start()
    th2 = Thread(target=fn2)
    th2.start()
    print('最终的num为：%s'%num)

if __name__ == '__main__':
    main()
