# -*- coding:utf-8 -*-

'多个线程调用同一个函数，各自执行各自的代码，不共享局部变量'

__author__ = '建磊'

import time
from threading import Thread
from threading import current_thread

def main():

    def fn():
        name = current_thread().name
        num = 0
        print('局部变量num的初始值为：%s'%num)
        if name == 'Thread-1':
            num += 1
        else:
            time.sleep(1)
        print('线程的名字是：%s，局部变量num的值为：%s'%(name,num))

    th1 = Thread(target=fn)
    th1.start()
    th2 = Thread(target=fn)
    th2.start()

if __name__ == '__main__':
    main()
