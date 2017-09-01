# -*- coding:utf-8 -*-

"多线程threading初体验"

__author__ = '建磊'

import threading
import time

def func(index):
    print('子线程%s'%index)
    time.sleep(1)

def main():
    for x in range(5):
        th = threading.Thread(target=func,args=(x,))
        th.start()

if __name__ == '__main__':
    main()
