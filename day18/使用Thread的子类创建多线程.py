# -*- coding:utf-8 -*-

"使用threading.Thread的子类创建多线程"

__author__ = '建磊'

import threading
import time

def main():
    class MyThread(threading.Thread):

        def run(self):
            for x in range(5):
                time.sleep(1)
                print('我的名字是：%s，index：%s'%(self.name,x))

    myThread = MyThread()
    myThread.start()


if __name__ == '__main__':
    main()
