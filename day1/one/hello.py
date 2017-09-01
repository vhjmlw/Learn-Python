#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

'这里是一个文档注释，hello模块的文档注释'

__author__ = '建磊'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print(args)
    elif len(args) == 2:
        print(args)
    else:
        print(args)

if __name__ == '__main__':
    test()
