# -*- coding:utf-8 -*-

'打印进度条'

__author__ = '建磊'

import time

def main():
    for x in range(100):
        print('\r%.2f%%'%x,end='')
        time.sleep(0.1)

if __name__ == '__main__':
    main()
