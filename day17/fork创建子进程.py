# -*- coding:utf-8 -*-

"fork创建子进程"

__author__ = "建磊"

import os
import time

id = os.fork()
if id == 0:
    while True:
        print('---子---')
        time.sleep(1)
else:
    while True:
        print('---父---')
        time.sleep(1)

