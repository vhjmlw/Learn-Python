# -*- coding:utf-8 -*-

'使用#显示进度条'

__author__ = '建磊'

import time

def main():
    for x in range(100):
        print('\r' + '#'*(x+1), end='')
        time.sleep(0.05)

if __name__ == '__main__':
    main()
