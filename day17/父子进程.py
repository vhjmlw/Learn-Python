# -*- coding:utf-8 -*-

"父子进程的顺序"

__author__ = '建磊'

import os
import time

id = os.fork()
if id == 0:
    print('---子---start')
    time.sleep(5)
    print('---子---end')
else:
    print('---父---start')
    time.sleep(3)
    print('---父---end')

print('over')
